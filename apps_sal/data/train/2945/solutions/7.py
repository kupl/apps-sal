def fortune(f0, p, c0, n, i):
    print(f0, p, c0, n, i)
    for _ in range(n-1):
        f0 = f0 * (100 + p) // 100 - c0
        c0 = c0 * (100 + i) // 100
    
    return f0 >= 0
