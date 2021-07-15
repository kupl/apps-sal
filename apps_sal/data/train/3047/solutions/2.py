import re

def repeating_fractions(num, den):
    d, f = str(num / den).split(".")
    return "{}.{}".format(d, re.sub(r"(\d)\1+", r"(\1)", f))
