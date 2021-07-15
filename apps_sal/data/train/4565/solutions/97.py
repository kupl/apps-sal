import re
def replace_dots(string):
    return string.replace(".","-") if "." in string or string == '' else "no dots"
