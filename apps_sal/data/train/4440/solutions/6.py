import re

def validate_pin(pin):
    return re.match(r'(?:\d{4}|\d{6})\Z', pin) is not None
