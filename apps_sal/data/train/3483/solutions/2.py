import re


def string_parse(s):
    if isinstance(s, str):
        return re.sub(r"(.)\1(\1+)", r"\1\1[\2]", s)
    return "Please enter a valid string"
