import re

def clean_text(message):
    message = message.lower()
    message = re.sub(r'[^\w\s]', '', message)
    return message