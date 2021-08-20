import re


def validate_pin(pin):
    return True if re.match('^(?:\\d{4}|\\d{6})\\Z', pin) else False
