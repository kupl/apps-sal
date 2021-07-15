def nth_chandos_number(n):
    t, ans = 1, 0
    while n:
        t *= 5
        if n % 2:
            ans += t
        n //= 2
    return ans
