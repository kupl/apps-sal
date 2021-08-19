from collections import Counter


def find_uniq(arr):
    c = Counter(''.join(arr).lower())
    match = [string_ for string_ in arr if min(c, key=c.get) in string_.lower()]
    return match[0]
