import re

def area_code(text):
    ac = re.search('\((\d{3})\)\s\d{3}\-\d{4}', text)
    return ac.group(1)
