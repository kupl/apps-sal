def find(n):
    a = n // 3 * (n // 3 + 1) // 2 * 3
    b = n // 5 * (n // 5 + 1) // 2 * 5
    c = n // 15 * (n // 15 + 1) // 2 * 15
    return a + b - c
