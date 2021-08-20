from math import sqrt


def list_squared(m, n):
    result = []
    for a in range(m, n + 1):
        total = 0
        for i in range(1, int(sqrt(a)) + 1):
            if a % i == 0:
                total += i ** 2
                if i < a / i:
                    total += (a / i) ** 2
        if sqrt(total) % 1 == 0:
            result.append([a, total])
    return result
