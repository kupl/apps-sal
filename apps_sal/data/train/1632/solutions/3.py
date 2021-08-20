def sumOnes(n):
    return (lambda msb: n and -~n + ~-msb * 2 ** msb + sumOnes(n - 2 ** (-~msb)))(n.bit_length() - 2)


def countOnes(a, b):
    return sumOnes(b) - sumOnes(a - 1)
