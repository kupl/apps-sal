import re


def reverse_letter(string):
    return ''.join(re.findall('[A-Za-z]', string)[::-1])
