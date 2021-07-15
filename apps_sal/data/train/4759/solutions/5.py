import re

def to_acronym(s):
    return ''.join(re.findall(r'\b(\w)', s)).upper()
