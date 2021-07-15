import re

def is_valid(idn):
    pattern = r'^[a-zA-z_\$]+[\w\$]*$'
    return bool(re.match(pattern, idn))
