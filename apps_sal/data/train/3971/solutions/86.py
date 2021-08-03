def tidyNumber(n):
    s = str(n)
    for c in list(zip(s[1:], s)):
        if c[0] < c[1]:
            return False
    return True
