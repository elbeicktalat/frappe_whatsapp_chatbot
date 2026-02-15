import frappe
from frappe.model.document import Document


class WhatsAppFlowStep(Document):
    def validate(self):
        if self.input_type == "Condition":
            self.validate_condition_logic()
        elif self.input_type == "Router":
            self.validate_router_logic()
        elif self.input_type == "Jump":
            self.validate_jump_logic()
        else:
            if not self.message and self.input_type != "None":
                frappe.throw(f"Message is required for visible step: {self.step_name}")

    def validate_condition_logic(self):
        if not self.response_script:
            frappe.throw(f"Condition '{self.step_name}' requires a script.")
        if not self.else_next_step:
            frappe.throw(f"Condition '{self.step_name}' requires an 'Else Next Step' for the False path.")

    def validate_router_logic(self):
        if not self.response_script:
            frappe.throw(f"Router '{self.step_name}' requires a script.")
        if not self.conditional_next:
            frappe.throw(f"Router '{self.step_name}' requires JSON paths in 'Conditional Next Step'.")

    def validate_jump_logic(self):
        if not self.next_step:
            frappe.throw(f"Jump step '{self.step_name}' must have a 'Next Step' to jump to.")
