def is_interesting(n, awesome_phrases):
    import math
    for m in range(3):
        s = str(n + m)
        if len(s) > 2 and (zf(s) or sd(s) or seqinc(s) or seqdec(s) or pal(s) or awe(s, awesome_phrases)):
            if m == 0:
                return 2
            else:
                return 1
    return 0


def awe(s, l):
    return s in [str(x) for x in l]


def pal(s):
    return s == s[::-1]


def seqdec(s):
    a = '9876543210'
    for i in range(len(s) - 1):
        if a.index(s[i]) + 1 != a.index(s[i + 1]):
            return False
    return True


def seqinc(s):
    a = '1234567890'
    for i in range(len(s) - 1):
        if a.index(s[i]) + 1 != a.index(s[i + 1]):
            return False
    return True


def sd(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            return False
    return True


def zf(s):
    for i in range(1, len(s)):
        if s[i] != '0':
            return False
    return True
