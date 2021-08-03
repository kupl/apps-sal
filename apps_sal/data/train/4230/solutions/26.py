import re


def reverse_letter(string):
    return re.sub(r"[^a-z]", "", string[::-1])
