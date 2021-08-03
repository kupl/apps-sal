def solve(s):
    n = 0
    for i in s:
        n += int(i.isupper())
    if n > len(s) // 2:
        return s.upper()
    else:
        return s.lower()
