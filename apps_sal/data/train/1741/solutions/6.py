def five_by_2n(n):
    a = [1, 8, 95, 1183, 14824]
    
    while len(a) <= n:
        nxt = (15 * a[-1] - 32 * a[-2] + 15 * a[-3] - a[-4])  % 12345787
        a.append(nxt)
    
    return a[n]
