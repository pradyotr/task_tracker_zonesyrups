app_name = "task_tracker"
app_title = "Task Tracker"
app_publisher = "pradyotr"
app_description = "Task Assignment & Auto-Score Calculator"
app_email = "pradyotraina@gmail.com"
app_license = "unlicense"

fixtures = [
    "Dashboard",
    "Dashboard Chart",
    "Dashboard Chart Source"
]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "task_tracker",
# 		"logo": "/assets/task_tracker/logo.png",
# 		"title": "Task Tracker",
# 		"route": "/task_tracker",
# 		"has_permission": "task_tracker.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/task_tracker/css/task_tracker.css"
# app_include_js = "/assets/task_tracker/js/task_tracker.js"

# include js, css files in header of web template
# web_include_css = "/assets/task_tracker/css/task_tracker.css"
# web_include_js = "/assets/task_tracker/js/task_tracker.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "task_tracker/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "task_tracker/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "task_tracker.utils.jinja_methods",
# 	"filters": "task_tracker.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "task_tracker.install.before_install"
# after_install = "task_tracker.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "task_tracker.uninstall.before_uninstall"
# after_uninstall = "task_tracker.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "task_tracker.utils.before_app_install"
# after_app_install = "task_tracker.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "task_tracker.utils.before_app_uninstall"
# after_app_uninstall = "task_tracker.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "task_tracker.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"task_tracker.tasks.all"
	],
	"daily": [
		"task_tracker.tasks.daily"
	],
	"hourly": [
		"task_tracker.tasks.hourly"
	],
	"weekly": [
		"task_tracker.tasks.weekly"
	],
	"monthly": [
		"task_tracker.tasks.monthly"
	],
    "cron": {
        "30 8 * * *": [
            "task_tracker.api.send_automated_follow_up_email"
        ]
    }
}

# Testing
# -------

# before_tests = "task_tracker.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "task_tracker.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "task_tracker.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["task_tracker.utils.before_request"]
# after_request = ["task_tracker.utils.after_request"]

# Job Events
# ----------
# before_job = ["task_tracker.utils.before_job"]
# after_job = ["task_tracker.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"task_tracker.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

