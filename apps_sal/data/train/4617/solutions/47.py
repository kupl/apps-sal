def powers_of_two(n):
    new_list = list(range(0, n+1))
    return [ 2 ** x for x in new_list ]
