import math


def list_squared(m, n):
    print(f'm: {m}, n: {n}', flush=True)
    biglips = []
    for i in range(m, n):
        if i > 2000 and i < 4000:
            i = 4000
        max = i + 1
        factors = []
        counter = 1
        while counter < max:
            if i % counter == 0:
                factors.append(counter)
                max = int(i / counter)
                if max != counter:
                    factors.append(max)
            else:
                max -= 1
            counter += 1
        factors = list(map(lambda x: x ** 2, factors))
        sumOf = sum(factors)
        root = math.sqrt(sumOf)
        if sumOf == int(root + 0.5) ** 2:
            biglips.append([i, sumOf])
    print(biglips)
    return biglips
