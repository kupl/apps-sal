import re

def string_parse(string):
    if not type(string) == str:
        return "Please enter a valid string"
    
    return re.sub(r'(([a-zA-Z])\2)(\2+)', lambda x: x.group(1) + '[' + x.group(3) + ']', string)
