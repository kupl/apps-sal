def lcm_cardinality(n):
    ans = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            t = 0
            while n % i == 0:
                n /= i
                t += 1
            ans *= t * 2 + 1
    if n > 1:
        ans *= 3
    return int(((ans - 1) / 2) + 1)
