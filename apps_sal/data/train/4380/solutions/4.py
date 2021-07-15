import re

def remove_chars(s):
    return re.sub(r"[^a-zA-Z\s]", "", s)
