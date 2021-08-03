import re


def sursurungal(txt):
    def change(t1):
        a, b = t1.split()
        if int(a) <= 1:
            return t1
        if int(a) == 2:
            return "{} bu{}".format(a, b[:-1]) if b[-1] == 's' else "{} bu{}".format(a, b)
        if int(a) <= 9:
            return "{} {}zo".format(a, b[:-1]) if b[-1] == 's' else "{} {}zo".format(a, b)
        else:
            return "{} ga{}ga".format(a, b[:-1]) if b[-1] == 's' else "{} ga{}ga".format(a, b)

    lst = re.findall("[0-9]+\s[a-zA-Z]+[\n]?", txt)
    lst = [i[:-1] if i[-1:] == '\n' else i for i in lst]
    t = txt[:]
    for i in lst:
        t = re.sub(i, '~', t)
    lst2 = [change(i) for i in lst]
    for i in lst2:
        t = t.replace('~', i, 1)
    return t
