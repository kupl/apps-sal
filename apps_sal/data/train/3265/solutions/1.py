def mult_triangle(n):
    k = n * (n + 1) // 2
    p = ((n + 1) // 2)**4
    return [k * k, k * k - p, p]
