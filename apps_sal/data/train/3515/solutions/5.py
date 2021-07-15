from string import ascii_lowercase as AL
import re

def f(op):
    def g(s, key):
        a = "".join(dict.fromkeys(key + AL))
        d = {x: i for i, x in enumerate(a)}
        def f(s):
            s, r = s[0], []
            for i, x in enumerate(s, 1):
                y = a[(op(d[x.lower()], i)) % len(a)]
                if x.isupper():
                    y = y.upper()
                r.append(y)
            return "".join(r)
        return re.sub(r"\w+", f, s)
    return g

encode = f(int.__add__)
decode = f(int.__sub__)
