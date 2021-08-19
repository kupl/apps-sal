def triplet(n):
    for i in range(int(n ** 0.333), 1, -1):
        if n % i:
            continue
        c = n // i
        for j in range(int(c ** 0.5), i, -1):
            if c % j or j == c // j:
                continue
            yield (i, j, c // j)


def pythagorean_triplet(n):
    for (a, b, c) in triplet(n):
        if a ** 2 + b ** 2 == c ** 2:
            return [a, b, c]
