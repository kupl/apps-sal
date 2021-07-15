def alternateCase(s):
    ans = ''
    for c in s:
        if c.upper() == c:
            ans += c.lower()
        elif c.lower() == c:
            ans += c.upper()
    return ans
