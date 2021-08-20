def tidyNumber(n):
    s = str(n)
    return all((x <= y for (x, y) in zip(s, s[1:])))
