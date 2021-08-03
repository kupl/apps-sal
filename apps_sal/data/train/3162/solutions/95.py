import re


def compare(s1, s2):
    def v(s): return "" if not s or re.search('[^a-zA-Z]', s) else s
    def c(s): return sum(ord(ch) for ch in s.upper())
    return c(v(s1)) == c(v(s2))
