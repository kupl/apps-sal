def sort_by_bit(x):
    on_bits = [f'{i:b}'.count('1') for i in x]
    sorted_tups = sorted(zip(on_bits, x))
    return list(list(zip(*sorted_tups))[1])
