def sum_two_smallest_numbers(L):
    x = min(L)
    L.remove(x)
    y = min(L)
    return x + y
