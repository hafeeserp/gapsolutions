# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gap_solutions"
app_title = "Gap Solutions"
app_publisher = "Hafees Kazhunkil"
app_description = "App for Gap Solutions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hafeesk@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gap_solutions/css/gap_solutions.css"
# app_include_js = "/assets/gap_solutions/js/gap_solutions.js"

# include js, css files in header of web template
# web_include_css = "/assets/gap_solutions/css/gap_solutions.css"
# web_include_js = "/assets/gap_solutions/js/gap_solutions.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {"Salary Slip" : "public/js/salary_slip.js"}
fixtures = [{"dt": "Custom Field", "filters":[["name", "in", ["Salary Slip-arrears_calculation","Salary Slip-increment_percentage","Salary Slip-pending_months_for_increment","Salary Slip-column_break_39","Salary Slip-increment_amount","Salary Slip-total_arrears","Department-increment_percentage"]]]}]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gap_solutions.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gap_solutions.install.before_install"
# after_install = "gap_solutions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gap_solutions.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gap_solutions.tasks.all"
# 	],
# 	"daily": [
# 		"gap_solutions.tasks.daily"
# 	],
# 	"hourly": [
# 		"gap_solutions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gap_solutions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gap_solutions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gap_solutions.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gap_solutions.event.get_events"
# }

