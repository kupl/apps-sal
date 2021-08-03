import re
P = re.compile('\([^\(\)]*\)')


def remove_parentheses(s):
    if '(' in s:
        return remove_parentheses(P.sub('', s))
    return s
