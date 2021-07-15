import re

def compare(s1, s2):
    v = lambda s: "" if not s or re.search('[^a-zA-Z]', s) else s
    c = lambda s: sum(ord(ch) for ch in s.upper())
    return c(v(s1)) == c(v(s2))

