def _sum(s):
    return (
        sum(ord(c) for c in s.upper())
        if s and s.isalpha()
        else 0)


def compare(s1, s2):
    return _sum(s1) == _sum(s2)

