import re
def replace_dots(str):
    if '.' in str:
        return str.replace(".", "-")
    else:
        return str
