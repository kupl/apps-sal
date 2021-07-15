import re

def validPhoneNumber(phoneNumber):
    pattern = "^\(\d{3,3}\) \d{3,3}-\d{4,4}$"
    compiled_pattern = re.compile(pattern)
    return True if re.match(compiled_pattern, phoneNumber) else False
