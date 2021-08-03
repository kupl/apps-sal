import re


def solve(s):
    uppercase = len(re.findall('[A-Z]', s))
    lowercase = len(re.findall('[a-z]', s))
    numbers = len(re.findall('[0-9]', s))
    special = len(re.findall('[^A-Za-z0-9]', s))
    return [uppercase, lowercase, numbers, special]
