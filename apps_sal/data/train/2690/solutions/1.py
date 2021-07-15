import re

def remove_parentheses(s):
    while (t := re.sub(r'\([^()]*\)', '', s)) != s:
        s = t
    return s
