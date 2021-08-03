def sxore(n):
    m = n % 4
    if m == 0:
        return n
    if m == 1:
        return 1
    if m == 2:
        return n + 1
    return 0
