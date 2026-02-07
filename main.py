from open_ai import analyse_email
from sheets import log_task
import json

email ="""
Hi my name is John Doe and I am interested in your product. Can you provide more information about the pricing and features? Thank you!
"""

result = analyse_email(email)
data = json.loads(result)

log_task(data)

print("Email analysis complete and logged to Google Sheets.", data)