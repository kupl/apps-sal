import re

def validate_pin(pin):
    return bool(re.search('^[0-9]{4}\Z$|^[0-9]{6}\Z$', pin))
