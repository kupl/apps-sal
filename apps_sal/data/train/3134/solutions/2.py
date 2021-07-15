import re

def is_valid(identifier):
    return bool(re.fullmatch(r"[a-z_$][\w$]*", identifier, flags=re.IGNORECASE))
