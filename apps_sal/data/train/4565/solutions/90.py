import re
def replace_dots(str):
    if str == "":
        return re.sub(r".", "-", str)
    return str.replace(".", "-")
