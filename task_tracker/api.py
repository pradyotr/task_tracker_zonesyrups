import frappe
import pandas as pd
from openai import OpenAI
from frappe.utils import get_bench_path
from datetime import datetime, timedelta

OPEN_AI_KEY = None

@frappe.whitelist()
def send_automated_follow_up_email():
    
    file_name = 'Project Data Sheet 3.csv'
    PATH_TO_SHEET = f"{get_bench_path()}/apps/task_tracker/files/{file_name}"
    
    check_date = datetime.now() - timedelta(days=60)
    
    data = pd.read_csv(PATH_TO_SHEET)
    
    data['Last Order Date'] = pd.to_datetime(data['Last Order Date'])
    
    filtered_customers = data[ data['Last Order Date'] < check_date ][['Customer Name', 'Email', 'Last 3 Items Ordered']]
    for index, row in filtered_customers.iterrows():
        generate_and_send_mail(row['Customer Name'], row['Email'], row['Last 3 Items Ordered'], OPEN_AI_KEY)
        
def generate_and_send_mail(customer_name, email, last_3_items_ordered, key):
    
    log_object = {
        "doctype": "Automated Email Log",
        "customer_name": customer_name,
        "sent_date": frappe.utils.today()
    }
    
    if not OPEN_AI_KEY:
        frappe.log_error('Open AI API Key not defined', 'Please enter the Open AI API key to get responses.')
        log_object['error'] = 'Open AI API Key not defined, please enter the Open AI API key to get responses.'
    else:
        client = OpenAI(api_key=key)
        prompt = f"Generate a sales reminder email for a customer named {customer_name} who last placed an order more than 2 months ago and the last 3 items ordered were {last_3_items_ordered}. Reply with just the email body."
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        if response.status == 'completed':
            
            frappe.sendmail(
                recipients = [email],
                subject = f"We Miss You, {customer_name} - Let's Restock Your Favourites",
                message=response.output_text
            )
            log_object['prompt'] = prompt
            log_object['email_snippet'] = response.output_text
        else:
            log_object['error'] = 'Response creation failed from Open AI'
    
    frappe.get_doc(log_object).insert()
    frappe.db.commit()
    