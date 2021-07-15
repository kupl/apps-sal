def get_factors(n):
    r = []
    k = 2
    while k*k <= n:
        if n % k == 0:
            cnt = 0
            while n % k == 0:
                n /= k
                cnt += 1
            r.append((k, cnt))
        k += 1
    if n > 1:
        r.append((n, 1))
    return r

def trailing_zeros(num, base):
    factors = get_factors(base)
    zeros = 1<<10000 # infinity
    for f, p in factors:
        cnt = 0
        k = f
        while k <= num:
            cnt += num // k
            k *= f
        zeros = min(zeros, cnt // p)
    return zeros
