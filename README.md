# Frappe WhatsApp Chatbot

A comprehensive chatbot solution for Frappe WhatsApp integration. Supports keyword-based replies, multi-step conversation flows, and optional AI-powered responses.

## Features

- **Keyword-Based Replies**: Configure automatic responses based on keywords
- **Conversation Flows**: Multi-step decision trees with user input collection
- **Optional AI Integration**: OpenAI and Anthropic support for intelligent responses
- **Session Management**: Track user conversations and handle timeouts
- **Business Hours**: Restrict bot responses to business hours
- **Flexible Configuration**: All settings managed via Frappe Desk UI

## Installation

```bash
# Inside your Frappe bench
bench get-app https://github.com/your-repo/frappe_whatsapp_chatbot
bench --site your-site install-app frappe_whatsapp_chatbot
```

## Requirements

- Frappe Framework >= 15.0.0
- frappe_whatsapp app (must be installed first)

### Optional (for AI features)

```bash
pip install openai      # For OpenAI integration
pip install anthropic   # For Anthropic Claude integration
```

## Configuration

### 1. Enable Chatbot

Navigate to **WhatsApp Chatbot** settings and:
- Check **Enabled**
- Select the WhatsApp Account (or enable "Process All Accounts")
- Set a default response message

### 2. Create Keyword Replies

Go to **WhatsApp Keyword Reply** list and create rules:

| Field | Description |
|-------|-------------|
| Keywords | Comma-separated keywords (e.g., "hello, hi, hey") |
| Match Type | Exact, Contains, Starts With, or Regex |
| Response Type | Text, Template, Media, or Flow |
| Priority | Higher priority rules match first |

### 3. Create Conversation Flows

Go to **WhatsApp Chatbot Flow** to create multi-step conversations:

1. Define trigger keywords
2. Add flow steps with:
   - Message to display
   - Input type (Text, Number, Email, Phone, Date, Select, Button)
   - Variable name to store user input
   - Next step (or conditional branching)
3. Set completion message and action

### 4. Optional: AI Configuration

In **WhatsApp Chatbot** settings:
1. Enable AI Responses
2. Select provider (OpenAI or Anthropic)
3. Enter API key
4. Configure model, temperature, and system prompt

Create **WhatsApp AI Context** documents to provide knowledge to the AI.

## DocTypes

| DocType | Purpose |
|---------|---------|
| WhatsApp Chatbot | Global settings (single) |
| WhatsApp Keyword Reply | Keyword-to-response mappings |
| WhatsApp Chatbot Flow | Conversation flow definitions |
| WhatsApp Flow Step | Steps within flows (child table) |
| WhatsApp Chatbot Session | Track active conversations |
| WhatsApp AI Context | Knowledge base for AI responses |

## Example Flow: Lead Collection

```
Flow Name: Contact Sales
Trigger Keywords: sales, contact, demo

Steps:
1. step_name: Ask for name
   message: "Great! I'd love to help. What's your name?"
   input_type: Text
   store_as: customer_name

2. step_email: Ask for email
   message: "Thanks {customer_name}! What's your email?"
   input_type: Email
   store_as: customer_email

3. step_company: Ask for company
   message: "And which company are you from?"
   input_type: Text
   store_as: company_name

Completion Message: "Thank you {customer_name}! Our sales team will contact you at {customer_email} shortly."

On Complete Action: Create Document
DocType: Lead
Field Mapping: {
  "lead_name": "customer_name",
  "email_id": "customer_email",
  "company_name": "company_name"
}
```

## Processing Priority

When a message is received, the chatbot processes it in this order:

1. **Active Flow Session** - Continue ongoing conversation
2. **Keyword Match** - Check keyword rules
3. **Flow Trigger** - Check flow trigger keywords
4. **AI Fallback** - Generate AI response (if enabled)
5. **Default Response** - Send default message

## API/Hooks

The chatbot hooks into WhatsApp Message creation:

```python
# hooks.py
doc_events = {
    "WhatsApp Message": {
        "after_insert": "frappe_whatsapp_chatbot.chatbot.processor.process_incoming_message"
    }
}
```

## Scheduled Jobs

- **Hourly**: Clean up expired sessions and send timeout messages

## License

MIT
