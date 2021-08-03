def max_tri_sum(numbers):
    snumbers = set(numbers)
    snumbersl1 = list(snumbers)
    snumbersl1 = sorted(snumbersl1)

    print(snumbers)
    snumbersl = []
    n = 3

    while n > 0:
        maxn = max(snumbersl1)
        snumbersl.append(maxn)
        n -= 1
        snumbersl1.pop()

    return sum(snumbersl)
