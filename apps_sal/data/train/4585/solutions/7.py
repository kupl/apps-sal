def find(a,b,n):
    r = [a, b]
    if n > 300:
        n = n % 300
    while len(r) <= n:
        x = r[-2] + r[-1]
        if x > 9:
            r.extend([x // 10, x % 10])
        else:
            r.append(x)
    return r[n]
