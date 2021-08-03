def even_numbers_before_fixed(a, n):
    return sum(i % 2 == 0 for i in a[:a.index(n)]) if n in a else -1
