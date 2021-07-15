import re

def area_code(text):
    return re.search(r'\((\d{3})\)',text).group(1)
