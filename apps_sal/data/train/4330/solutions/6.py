def shortest_arrang(n):
    for i in range(2, n):
        if (n / i) * 2 < i:
            break
        if i % 2 == 0 and (n / i) % 1 == 0.5:
            return [n // i - i // 2 + 1 + j for j in range(0, i)[::-1]]
        if i % 2 == 1 and (n / i) % 1 == 0:
            return [n // i - (i - 1) // 2 + j for j in range(0, i)[::-1]]
    return [-1]
