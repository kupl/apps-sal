import re


def remove_parentheses(s):
    ret, count = "", 0
    for letter in s:
        if letter == "(":
            count += 1
        elif letter == ")":
            count -= 1
        elif count == 0:
            ret += letter
    return ret
