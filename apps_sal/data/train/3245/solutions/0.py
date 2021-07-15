def checkchoose(m, n):
    c = 1
    for x in range(n // 2 + 1):
        if c == m: return x
        c = c * (n-x) // (x+1)
    else: return -1

