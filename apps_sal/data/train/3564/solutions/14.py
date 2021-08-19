def stringy(size):
    return ''.join(('0' if x % 2 else '1' for x in range(size)))
