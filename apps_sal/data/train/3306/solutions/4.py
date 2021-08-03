def solve(a, b):
    s = a.find("*")
    if s == -1:
        return a == b
    else:
        a = list(a)
        b = list(b)
        del b[s:s + 1 + len(b) - len(a)]
        a.remove("*")
        return a == b
