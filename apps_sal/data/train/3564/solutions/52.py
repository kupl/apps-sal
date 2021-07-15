def stringy(size):
    return ''.join(str(x & 1) for x in range(1, size+1))
