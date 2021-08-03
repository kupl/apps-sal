import collections


def letter_count(s):
    result = {}
    for i, d in enumerate(s):
        count = 1
        if d not in result:
            for j in range(i + 1, len(s)):
                if d == s[j]:
                    count += 1
            result[d] = count
    return collections.OrderedDict(sorted(result.items()))
