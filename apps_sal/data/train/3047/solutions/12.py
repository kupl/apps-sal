import re


def repeating_fractions(a, b):
    if not a % b:
        return str(a / b)
    a, b = str(a / b).split(".")
    return a + "." + re.sub(r"(.)\1+", r"(\1)", b)
