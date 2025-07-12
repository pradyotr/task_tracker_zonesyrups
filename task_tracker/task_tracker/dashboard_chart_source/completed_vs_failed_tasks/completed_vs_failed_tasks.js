frappe.dashboards.chart_sources["Completed vs Failed Tasks"] = {
	method: "task_tracker.task_tracker.dashboard_chart_source.completed_vs_failed_tasks.completed_vs_failed_tasks.get",
	filters: [
		{
			fieldname: "assigned_to",
			label: __("Person"),
			fieldtype: "Link",
			options: "User"
		}
	]
}