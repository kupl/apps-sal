import re
span = "<span style=\"color: {0}\">{1}</span>"
subs = {
    "F": "pink", 
    "L": "red",
    "R": "green",
    "digit": "orange"
}


def sub(match):
    char = match.group(0)[0]
    if char.isdigit():
        return span.format(subs["digit"], match.group(0))
    else:
        return span.format(subs[char], match.group(0))

def highlight(code):
    return re.sub("(F+|L+|R+|[0-9]+)", sub, code) 
