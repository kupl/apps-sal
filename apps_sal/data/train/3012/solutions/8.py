def shared_bits(a, b):
    (bina, binb) = ('{:011b}'.format(a), '{:011b}'.format(b))
    return sum((1 for (x, y) in zip(bina, binb) if x == y == '1')) >= 2
