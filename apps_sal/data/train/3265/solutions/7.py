def mult_triangle(n):
    n2 = n - 1 | 1
    total_sum = ((n+1) * n // 2)**2
    total_odd_sum = ((n2+1) * (n2+1) // 4)**2
    return [total_sum, total_sum - total_odd_sum, total_odd_sum]
