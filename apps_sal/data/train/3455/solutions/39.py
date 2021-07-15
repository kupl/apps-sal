def disarium_number(n):
    s = str(n)
    sm = 0
    for i in range(len(s)):
        sm += int(s[i]) ** (i + 1)
    if sm == n:
        return "Disarium !!"
    return "Not !!"

