import re
def area_code(text):
    return re.search(r'\((.*)\)',text).group(1)
