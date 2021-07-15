import re
def replace_dots(str):
    a = re.sub(r"\.", "-", str)
    return a
