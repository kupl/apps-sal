def big_primefac_div(n):
    if n % 1:
        return "The number has a decimal part. No Results"
    o = n = abs(int(n))
    mn, mx = 0, 1
    while n % 2 == 0:
        mn, mx, n = mn or 2, 2, n//2
    k = 3
    while k*k <= n:
        if n % k:
            k = k+2
        else:
            mn, mx, n = mn or k, k, n//k
    return [max(mx, n), o//mn] if mn else []

