import frappe
import json
from frappe import _
from frappe.utils import getdate, today, date_diff

@frappe.whitelist()
def get(
    chart_name=None,
	chart=None,
	no_cache=None,
	filters=None,
	from_date=None,
	to_date=None,
	timespan=None,
	time_interval=None,
	heatmap_year=None,
    ):
    
    user = json.loads(filters).get("assigned_to") if filters else None
    
    current_day = getdate(today())

    res = frappe.db.get_list("Task Tracker", fields=["assigned_to", "task_name" , "original_due_date", "revised_due_date", "extension_count"])

    labels = []
    values = []

    for row in res:
        if user and row.assigned_to != user:
            continue
        overdue_date = row.revised_due_date if row.revised_due_date else row.original_due_date
    
        if current_day > overdue_date:
            labels.append(row.task_name)
            values.append(frappe.utils.date_diff(current_day, overdue_date))

    return {
		"labels": labels,
		"datasets": [{"name": _("Task Tracker"), "values": values}]
	}