import re


def problem(a):
    if re.match(r"\d", str(a)):
        return (a * 50) + 6
    else:
        return "Error"
