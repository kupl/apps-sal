def mult_triangle(n):
    total = (n * (n + 1) // 2) ** 2
    odd = ((n + 1) // 2) ** 4
    even = total - odd
    return [total, even, odd]
