def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))
