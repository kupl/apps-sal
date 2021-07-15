import re

def drop_cap(s):
    return re.sub(r'\S{3,}', lambda m: m.group(0).title(), s)
