def sum_even_numbers(seq):
    L = []
    for i in seq:
        if i % 2 == 0:
            L.append(i)
    return sum(L)
