import re


def bracket_buster(string):
    return re.findall('\\[(.*?)\\]', string) if type(string) == str else 'Take a seat on the bench.'
