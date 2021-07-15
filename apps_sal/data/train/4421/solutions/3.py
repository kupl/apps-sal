import re
from functools import reduce

HH_MM_SS_PATTERN = re.compile(r'\A(\d\d):([0-5]\d):([0-5]\d)\Z')


def to_seconds(time):
    m = HH_MM_SS_PATTERN.search(time)
    if m:
        return reduce(lambda x, y: x * 60 + int(y), m.groups(), 0)
    return None

