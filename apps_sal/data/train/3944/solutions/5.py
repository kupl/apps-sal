def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    x, out = 1, [1]
    while n - 1 >= x:
        x += 1
        out.append(out[-1] + x)
    return sum(out)
