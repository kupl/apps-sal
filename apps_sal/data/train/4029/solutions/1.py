import re


def search_substr(origin, target, overlap=True):
    if not target:
        return 0
    (start, end) = map(re.escape, (target[0], target[1:]))
    patternStr = '{}{}'.format(start, f'(?={end})' if overlap else end)
    return sum((1 for _ in re.finditer(patternStr, origin)))
