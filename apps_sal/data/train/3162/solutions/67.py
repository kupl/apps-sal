def subCompare(s):
    t = 0
    if s is None or not s.isalpha():
        s = ''
    for x in s:
        t += ord(x.upper())
    return t


def compare(s1, s2):
    t1 = subCompare(s1)
    t2 = subCompare(s2)
    return t2 == t1
