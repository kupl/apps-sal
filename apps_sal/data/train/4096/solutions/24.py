import re


def valid_parentheses(string):
    s = ''.join([i for i in string if i in "()"])
    total = [string]
    while True:
        s = s.replace("()", "")
        total.append(s)
        if total[-1] == total[-2]:
            break
    return True if total[-1] == "" else False
