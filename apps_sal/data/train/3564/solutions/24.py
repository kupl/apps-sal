def stringy(size):
    return ''.join(('%d' % (not i % 2) for i in range(size)))
