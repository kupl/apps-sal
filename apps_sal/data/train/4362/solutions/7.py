import re


def frogify(s):
    a = re.split(r"([!?.])", s.translate(str.maketrans("", "", ",;()-")).strip())
    if not a[-1]:
        a.pop()
    return "".join(f(x) for x in a)


def f(s):
    return s if s in "!?." else " " * (s[0] == " ") + " ".join(s.strip().split()[::-1])
