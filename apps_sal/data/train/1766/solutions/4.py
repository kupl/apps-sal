import math


def convert_to_base(a, b):
    if a == 0:
        return 0

    remainders = []

    while a != 0:
        c = a / b
        if c < 1:
            c = math.ceil(c)
        else:
            c = math.floor(c)

        d = a - b * c
        while d < 0:
            c += 1
            d = a - b * c

        a = c
        remainders.append(str(int(d)))

    remainders.reverse()
    return int("".join(remainders))


def skrzat(base, number):
    if base == 'b':
        bits = reversed([int(bit) for bit in number])
        dec = 0
        for power, bit in enumerate(bits):
            dec += bit * ((-2)**power)

        return "From binary: {0} is {1}".format(number, dec)
    else:
        binary = convert_to_base(number, -2)
        return "From decimal: {0} is {1}".format(number, binary)
