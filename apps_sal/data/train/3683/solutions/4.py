import collections


def letter_count(s):
    res = collections.defaultdict(int)
    for _char in s:
        res[_char] += 1
    return res
