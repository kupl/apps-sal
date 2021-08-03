import re


def reverse_letter(string):
    str = re.sub("[^a-z]", "", string)
    return str[::-1]
