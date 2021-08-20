def pattern(n, x=1, *args):
    pat = [''.join([' ' * (i - 1), str(i % 10), ' ' * (n - i)]) for i in range(1, n + 1)]
    pat = [''.join([i, i[-2::-1]]) for i in pat]
    pat = [''.join([i, i[1:] * (x - 1)]) for i in pat]
    return '\n'.join(pat + pat[-2::-1])
