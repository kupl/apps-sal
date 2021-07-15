def lcm_cardinality(n):
    card = 1
    for d in range(2, int(n ** .5) + 1):
        if not n % d:
            mul = 0
            while not n % d:
                mul += 1
                n //= d
            card *= 2 * mul + 1
    if n > 1: card *= 3
    return (card + 1) // 2
