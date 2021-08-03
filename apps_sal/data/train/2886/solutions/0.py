import re


def find(stg):
    matches = re.findall(r"(!+|\?+)", stg)
    return max((f"{a}{b}" for a, b in zip(matches, matches[1:])), key=len, default="")
