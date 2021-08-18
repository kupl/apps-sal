REV = {'6': '9', '9': '6'}
BASE = set("01869")


def isReversible(n):
    s = str(n)
    return (not (set(s) - BASE)
            and (not len(s) % 2 or s[len(s) // 2] not in "69")
            and all(REV.get(c, c) == s[-1 - i] for i, c in enumerate(s[:len(s) // 2])))


def solve(a, b):
    return sum(isReversible(n) for n in range(a, b))
