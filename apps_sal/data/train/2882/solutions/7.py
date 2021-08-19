def cumulative_triangle(n):
    x = sum(range(n + 1))
    return sum(range(x - n + 1, x + 1))
