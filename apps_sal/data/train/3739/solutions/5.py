def branch(n):
    if n == 1:
        return 0
    l = (1 + int((n - 1 + 0.5) ** 0.5)) // 2
    x = (2 * l - 1) ** 2 + 1
    return (n - x) // (l * 2)
