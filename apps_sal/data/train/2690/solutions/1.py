import re


def remove_parentheses(s):
    while (t := re.sub('\\([^()]*\\)', '', s)) != s:
        s = t
    return s
