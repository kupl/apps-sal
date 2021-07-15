def stringy(size):
    return ''.join('{:d}'.format(not i % 2) for i in range(size))
