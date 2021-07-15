import re

def validate(message):
    return bool(re.match(
        r'MDZHB \d\d \d\d\d [A-Z]+( \d\d){4}$',
        message
    ))
