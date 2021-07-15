import re

def validate(message):
    return bool(re.match(r'MDZHB \d{2} \d{3} [A-Z]+( \d{2}){4}$', message))
