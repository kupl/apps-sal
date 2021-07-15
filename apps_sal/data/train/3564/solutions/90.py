def stringy(size):
    return ''.join([['1', '0'][loop % 2] for loop in range(size)])
