import re

def solve(s):
    rev = []
    for i in reversed(s):
        if i != " ":
            rev.append(i)

    spaces = re.compile(" ")
    for m in spaces.finditer(s):
        rev.insert(m.start(), " ")

    return "".join(rev)

