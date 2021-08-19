def tidyNumber(n):
    s = str(n)
    return ''.join(sorted(s)) == s
