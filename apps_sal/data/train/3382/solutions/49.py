import re


def lowercase_count(strng):
    lijst = re.findall('[a-z]', strng)
    return len(lijst)
