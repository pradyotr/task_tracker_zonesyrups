frappe.dashboards.chart_sources["Overdue Highlights"] = {
	method: "task_tracker.task_tracker.dashboard_chart_source.overdue_highlights.overdue_highlights.get",
	filters: [
		{
			fieldname: "assigned_to",
			label: __("Person"),
			fieldtype: "Link",
			options: "User"
		}
	]
}