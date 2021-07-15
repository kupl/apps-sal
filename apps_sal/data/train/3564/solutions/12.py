ONE_ZERO = '10'


def stringy(size):
    return ''.join(ONE_ZERO[a % 2] for a in range(size))

