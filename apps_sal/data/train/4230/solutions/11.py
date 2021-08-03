import re


def reverse_letter(string):
    return "".join(re.findall(r"[A-Za-z]", string)[::-1])
