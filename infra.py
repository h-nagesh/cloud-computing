cloud_models = {
    "IaaS": "Infrastructure as a Service (e.g., AWS EC2, Azure VMs)",
    "PaaS": "Platform as a Service (e.g., Google App Engine, Heroku)",
    "SaaS": "Software as a Service (e.g., Gmail, Dropbox, Salesforce)",
}

print("Cloud Computing Service Models\n")

for short_name, description in cloud_models.items():
    print(f"{short_name}: {description}")
