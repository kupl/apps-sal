import re

def to_alternating_case(string):
    return re.sub(r'([a-z])|([A-Z])',
        lambda c: (c.groups()[0] or "").upper() + (c.groups()[1] or "").lower(),
        string)
