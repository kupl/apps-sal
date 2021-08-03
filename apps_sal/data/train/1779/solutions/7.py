def balanced_parens(n): return rec(n, "(", list()) if n != int() else [""]


def rec(n, current, ways):
    if n > current.count("("):
        ways = rec(n, current + "(", ways)
        if current.count("(") > current.count(")"):
            ways = rec(n, current + ")", ways)
    else:
        ways += [current + (n - current.count(")")) * ")"]
    return ways
