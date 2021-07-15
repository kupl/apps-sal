def sum_triangular_numbers(n):
    return sum([sum([1+i for i in range(n)][:i+1]) for i in range(n)])
