import re


def spin_solve(sentence):

    def f(m):
        (s, punc) = m.groups()
        return (s[::-1] if len(s) > 6 or s.lower().count('t') >= 2 else s.upper() if len(s) == 2 or punc == ',' else '0' if len(s) == 1 else s) + punc
    return re.sub("([-'a-zA-Z]+)([,.?!]?)", f, sentence)
