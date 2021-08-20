import re


def validate_pin(pin):
    matches = re.findall('\\d', pin)
    if len(pin) == 4:
        return len(matches) == 4
    elif len(pin) == 6:
        return len(matches) == 6
    else:
        return False
