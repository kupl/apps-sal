import re
def replace_dots(str):
    replaced = re.sub(r'\.','-', str)
    return replaced
