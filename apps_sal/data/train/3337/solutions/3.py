import re

def bracket_buster(string):
    if not isinstance(string, str):
        return "Take a seat on the bench."
    return re.findall(r'\[(.*?)\]', string)

