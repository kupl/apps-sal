import re
def camelize(s):
    return "".join(map(str.capitalize, re.findall(r"[a-zA-Z0-9]+", s)))
