def list_squared(m, n):
    all = []
    for x in range(m, n):
        divisors = [i for i in range(1, int(x**0.5) + 1) if x % i == 0]
        divisors += [int(x / d) for d in divisors if x / d > x**0.5]
        sumExp = sum(d**2 for d in divisors)
        if sumExp**0.5 % 1 == 0:
            all.extend([[x, sumExp]])
    return all
