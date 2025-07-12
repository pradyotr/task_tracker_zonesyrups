import frappe
import json
from frappe import _

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
    assigned_to = f' AND assigned_to = "{user}"' if user else ''
    
    query = f"""
        SELECT (
            CASE
                WHEN score = 0 THEN 'Failed' ELSE 'Completed'
            END
        ) AS CorF, COUNT(*) AS Counts
        FROM `tabTask Tracker`
        WHERE 1=1 {assigned_to}
        GROUP BY CorF
    """
    
    res = frappe.db.sql(query, as_dict=True)
    print(query, res)
    labels = [x["CorF"] for x in res]
    values = [x["Counts"] for x in res]
    
    return {
		"labels": labels,
		"datasets": [{"name": _("Task Tracker"), "values": values}]
	}