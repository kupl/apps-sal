from collections import Counter


def numericals(s):
    def f(s):
        cnts = Counter()
        for c in s:
            cnts[c] += 1
            yield cnts[c]
    return ''.join(map(str, f(s)))
