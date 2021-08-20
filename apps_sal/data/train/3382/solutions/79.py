import re


def lowercase_count(strng):
    ct = 0
    for i in range(len(strng)):
        if re.search('[a-z]', strng[i]) != None:
            ct += 1
    return ct
