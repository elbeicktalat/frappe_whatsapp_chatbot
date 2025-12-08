from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="frappe_whatsapp_chatbot",
    version="0.0.1",
    description="WhatsApp Chatbot for Frappe with keyword replies, conversation flows, and optional AI",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
