import frappe
from frappe.model.document import Document


class WhatsAppFlowStep(Document):
    def validate(self):
        if self.input_type == "Router":
            self.validate_router_logic()
        else:
            if not self.message:
                frappe.throw(f"Message is required for visible step: {self.step_name}")

    def validate_router_setup(self):
        # 1. Ensure response_script is present
        if not self.response_script:
            frappe.throw(f"Step '{self.step_name}' is a Router and requires a 'Response Script' to decide the path.")

        if "response" not in self.response_script:
            frappe.throw("Router scripts usually need to set the 'response' variable to True or False.")

        # 2. Ensure else_next_step is present (so the logic has two paths)
        if not getattr(self, "else_next_step", None):
            frappe.throw(
                f"Step '{self.step_name}' is a Router and requires an 'Else Next Step' for when the script returns False."
            )

        # 3. Prevent Router Chaining (The "No Stack Overflow" check)
        if self.next_step:
            self.check_target_is_not_router(self.next_step, "Next Step")

        if self.else_next_step:
            self.check_target_is_not_router(self.else_next_step, "Else Next Step")

    def check_target_is_not_router(self, target_step_name, field_label):
        # Note: We use 'parent' to ensure we check steps within the same Chatbot Flow
        target_type = frappe.db.get_value(
            "WhatsApp Flow Step",
            {"step_name": target_step_name, "parent": self.parent},
            "input_type"
        )

        if target_type == "Router":
            frappe.throw(
                f"Logic Error: Router step '{self.step_name}' cannot point to another Router ('{target_step_name}'). "
                f"The {field_label} must be a visible step (Text, Button, etc.) to prevent infinite loops."
            )
