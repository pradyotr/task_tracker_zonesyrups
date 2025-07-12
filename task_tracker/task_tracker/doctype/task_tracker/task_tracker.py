# Copyright (c) 2025, pradyotr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TaskTracker(Document):
     
     def validate(self):
          if self.original_due_date < self.start_date:
               frappe.throw("Due Date cannot be less than Start Date.")
          self.score = (100 - 25*self.extension_count) if self.extension_count < 4 else 0