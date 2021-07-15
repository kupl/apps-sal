import re
def replace_dots(s):
    s = re.sub(r"\.", "-", s)
    return s 
