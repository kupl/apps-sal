(n, h) = list(map(float, input().split(' ')))
print(' '.join(['%.12f' % (((k + 1) / n) ** 0.5 * h) for k in range(int(n) - 1)]))
