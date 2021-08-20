import re


def validPhoneNumber(phoneNumber):
    if re.match('^\\([0-9]{3}\\) [0-9]{3}-[0-9]{4}$', phoneNumber):
        return True
    return False
