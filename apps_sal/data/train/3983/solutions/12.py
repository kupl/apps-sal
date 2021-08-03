def Xbonacci(signature, n):
    l = len(signature)
    t = signature
    i = l
    while i < n:
        t.append(sum(t[i - l:i]))
        i += 1
    return t[:n]
