import re

def validPhoneNumber(phoneNumber):
    return any(re.findall("^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$", phoneNumber))
