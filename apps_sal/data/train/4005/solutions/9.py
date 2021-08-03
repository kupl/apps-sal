def reverse_bits(n):

    b = "{0:b}".format(n)

    return int(b[::-1], 2)
