import re


def to_seconds(time):
    match = re.match('(\\d\\d):([0-5]\\d):([0-5]\\d)\\Z', time)
    return match and sum((int(n) * 60 ** i for (i, n) in enumerate(match.groups()[::-1])))
