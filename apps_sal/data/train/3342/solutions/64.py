def pattern(n):
    if n < 1:
        return ""
    s = []
    for i in range(1,n+1):
        s.append(i*str(i))
    return '\n'.join(s)
