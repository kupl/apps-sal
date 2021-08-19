cache = {}


def sum_cache(n):
    if n not in cache:
        divs = [i for i in range(1, n + 1) if n % i == 0]
        cache[n] = sum([x * x for x in divs])
        return cache[n]
    return cache[n]


def list_squared(m, n):
    # your code

    result = []
    for j in range(m, n + 1):
        summ = sum_cache(j)
        if (summ ** 0.5).is_integer():
            result.append([j, summ])

    return result
