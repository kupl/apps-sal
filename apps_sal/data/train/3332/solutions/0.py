import re

def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)
