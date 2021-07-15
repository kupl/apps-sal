def stringy(size):
    return ''.join(map(str, map(int, map(lambda x: not x % 2, range(size)))))
