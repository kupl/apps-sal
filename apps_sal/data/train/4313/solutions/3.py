from functools import reduce

BOX_DIM = 16


def box_capacity(*dims):
    return reduce(int.__mul__, (d * 12 // BOX_DIM for d in dims))
