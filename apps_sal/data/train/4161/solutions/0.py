def rat_at(n):
    if n == 0:
        return 1, 1
    a, b = rat_at((n - 1) // 2)
    return (a, a + b) if n % 2 else (a + b, b)

def index_of(a, b):
    if a == b == 1:
        return 0
    return 2 * index_of(a, b - a) + 1 if b > a else 2 * index_of(a - b, b) + 2
