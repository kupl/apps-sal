def lcm_cardinality(n):
    res = 1
    for i in [2] + list(range(3, int(n**0.5) + 1, 2)):
        count = 0
        while not n % i:
            n, count = n // i, count + 1
        res *= 2 * count + 1
    if n > 1:
        res *= 3
    return (res + 1) // 2
