import re

def is_letter(stg):
    return bool(re.match(r"[a-z]\Z", stg, re.I))
