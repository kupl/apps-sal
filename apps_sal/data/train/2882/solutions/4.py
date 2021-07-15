def cumulative_triangle(n):
    start = sum(range(n)) + 1
    return sum(range(start, start + n))
