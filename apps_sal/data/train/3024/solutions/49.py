import re


def friend(x):
    result = []
    for n in x:
        if re.match(r'\A....\Z', n):
            result.append(n)
    return result
