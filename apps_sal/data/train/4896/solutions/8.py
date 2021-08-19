from itertools import accumulate


def f(d, word):
    for c in accumulate(word):
        if c not in d:
            d[c] = {}
        d = d[c]


def replace(d):
    return {key: replace(value) for (key, value) in d.items()} if d else None


def build_trie(*words):
    d = {}
    for word in words:
        f(d, word)
    return replace(d) or {}
