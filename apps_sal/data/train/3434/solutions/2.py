def bin_mul(m,n):
    if m < n: return bin_mul(n,m)
    if n == 0: return[] 
    r = []
    while m >= 1:
        print(m,n)
        if m % 2: r.append(1*n)
        m = m//2
        n = n*2
    
    return sorted(r,reverse=True)
