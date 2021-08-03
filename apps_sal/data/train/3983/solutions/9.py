def Xbonacci(s, n):
    if n < len(s):
        return s[:n]
    x = len(s)
    for i in range(n - len(s)):
        s.append(sum(s[-x:]))
    return s
