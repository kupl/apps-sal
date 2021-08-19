def evil(n):
    n_as_bin_string = '{0:b}'.format(n)
    nof_ones = n_as_bin_string.count('1')
    return "It's Odious!" if nof_ones % 2 else "It's Evil!"
