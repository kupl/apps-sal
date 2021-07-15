import string

def to_alternating_case(str):
    return "".join(c.lower() if c in string.ascii_uppercase else c.upper() for c in str)
