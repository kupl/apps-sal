from collections import Counter


def answer(qs, info):
    (qs, option) = (Counter(qs.lower().split()), [])
    for i in info:
        c = sum((l == qs.get(k) for (k, l) in Counter(i.lower().split()).items()))
        option.append([c, i] if c else [0, None])
    return max(option)[1]
