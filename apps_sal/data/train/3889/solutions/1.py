import re
def area_code(text):
    return re.search("\((\d{3})\)", text).group(1)
