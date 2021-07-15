import re

def apparently(s):
    return re.sub(r"(and\b|but\b)( apparently\b)?", r"\1 apparently", s)
