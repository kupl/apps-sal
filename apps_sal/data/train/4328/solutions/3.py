import re


def friend_find(line):
    s = ' '.join(line)
    return len(re.findall('\\bblue blue red\\b|\\bblue red (?=blue\\b)|\\bred (?=blue blue\\b)', s))
