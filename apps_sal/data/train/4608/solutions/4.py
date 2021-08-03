def finance(n):
    return sum((i + 1) * 3 * i // 2 for i in range(1, n + 1))
