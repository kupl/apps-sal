def shortest_arrang(n):
    if n % 2 == 1:
        return [n // 2 + 1, n // 2]

    for i in range(3, n // 2):
        if i % 2 == 1 and n % i == 0:
            return list(range(n // i + i // 2, n // i - i // 2 - 1, -1))
        elif i % 2 == 0 and n % i == i // 2:
            return list(range(n // i + i // 2, n // i - i // 2, -1))

    return [-1]
