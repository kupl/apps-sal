def mult_triangle(n):
    total = (n * (n+1) // 2) ** 2
    odd = ((n + 1) // 2) ** 4
    return [total, total - odd, odd]
