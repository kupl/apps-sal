def count_sheep(n):
    sheeps = ("{} sheep...".format(i) for i in range(1, n + 1))
    return ''.join(sheeps)
