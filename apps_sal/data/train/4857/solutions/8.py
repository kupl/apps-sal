def square_up(n):
    return [n - j if n - j - 1 <= i else 0 for i in range(n) for j in range(n)]
