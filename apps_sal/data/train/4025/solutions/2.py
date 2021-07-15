def func(l):
    n = sum(l) // len(l)
    return [n] + '{:b} {:o} {:x}'.format(n, n, n).split()
