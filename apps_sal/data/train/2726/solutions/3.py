def square_it(d):
    return 'Not a perfect square!' if len(str(d)) ** 0.5 % 1 else ''.join((str(d)[i:i + int(len(str(d)) ** 0.5)] + '\n' for i in range(0, len(str(d)), int(len(str(d)) ** 0.5))))[:-1]
