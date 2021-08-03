def sum_triangular_numbers(n):
    # your code here
    if n > 0:
        z = 1
        x = []
        for i in range(2, n + 1):
            z = z + i
            x.append(z)
        return sum(x) + 1
    if n < 0:
        return 0
