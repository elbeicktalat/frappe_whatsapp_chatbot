import frappe
from frappe.model.document import Document


class WhatsAppChatbot(Document):
    def validate(self):
        if self.enable_ai:
            if not self.ai_provider:
                frappe.throw("Please select an AI Provider when AI is enabled")
            if not self.ai_api_key:
                frappe.throw("Please enter an API Key when AI is enabled")

        if self.business_hours_only:
            if not self.business_start_time or not self.business_end_time:
                frappe.throw("Please set business hours when 'Respond Only During Business Hours' is enabled")

        if self.ai_temperature and (self.ai_temperature < 0 or self.ai_temperature > 1):
            frappe.throw("AI Temperature must be between 0 and 1")
