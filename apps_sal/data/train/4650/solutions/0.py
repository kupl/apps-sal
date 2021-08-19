def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match('^(\\([0-9]+\\))? [0-9]+-[0-9]+$', phoneNumber))
