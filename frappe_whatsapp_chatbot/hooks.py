app_name = "frappe_whatsapp_chatbot"
app_title = "Frappe WhatsApp Chatbot"
app_publisher = "Your Name"
app_description = "WhatsApp Chatbot for Frappe with keyword replies, conversation flows, and optional AI"
app_email = "your@email.com"
app_license = "MIT"
required_apps = ["frappe"]

# Document Events
doc_events = {
    "WhatsApp Message": {
        "after_insert": "frappe_whatsapp_chatbot.chatbot.processor.process_incoming_message"
    }
}

# Scheduler Events
scheduler_events = {
    "hourly": [
        "frappe_whatsapp_chatbot.chatbot.session_manager.cleanup_expired_sessions"
    ]
}

# Fixtures - export these DocTypes when exporting fixtures
fixtures = []

# Website route rules
website_route_rules = []

# Desk modules
# Each module is linked to a workspace
# modules = [
#     {"module_name": "Frappe WhatsApp Chatbot", "category": "Modules"}
# ]
