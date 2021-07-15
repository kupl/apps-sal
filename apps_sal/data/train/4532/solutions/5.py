import re

def validate_code(code):
    return bool(re.match("^[1-3]",str(code)))
