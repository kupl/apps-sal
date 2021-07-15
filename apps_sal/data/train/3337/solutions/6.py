import re

def bracket_buster(string):
    if type(string) is not str:
        return "Take a seat on the bench."
    return re.findall(r'\[(.*?)\]', string)
