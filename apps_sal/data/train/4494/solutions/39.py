import re


def points(games):
    match = re.findall('[0-9]', ''.join(games))
    p = 0
    for i in range(0, len(match), 2):
        if ord(match[i]) > ord(match[i + 1]):
            p += 3
        elif ord(match[i]) == ord(match[i + 1]):
            p += 1
    return p
