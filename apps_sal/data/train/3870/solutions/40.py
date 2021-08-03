def solve(s):
    d = ""
    for i in range(len(s)):
        el = s[i]
        if el.isalpha():
            d = el + d
    for i in range(len(s)):
        el = s[i]
        if el == ' ':
            d = d[:i] + el + d[i:]
    return d
