def mult_triangle(n):
    total = (n * (n + 1) / 2)**2
    odds = ((n + 1) // 2)**4
    return [total, total - odds, odds]

