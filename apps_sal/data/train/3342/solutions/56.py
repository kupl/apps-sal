def pattern(n):
    if n < 0:
        return ""
    ans = []
    pattern = []
    count = n
    while n > 0:
        n = str(n)
        pattern.append(n)
        if len(pattern) == int(n):
            ans.insert(0, "".join(pattern))
            n = int(n)
            n -= 1
            pattern = []
        n = int(n)
    return "\n".join(ans)
