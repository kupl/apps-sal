def sum_triangular_numbers(n):
    if n < 1:
        return 0
    else:
        triangular = []
        for i in range(1, n+1):
            triangular.append(i*(i+1)/2)
        return int(sum(triangular))
