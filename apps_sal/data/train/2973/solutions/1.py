array_conversion = c = lambda a, p=0: a[1:] and c([[x + y, x * y][p]for x, y in zip(*[iter(a)] * 2)], 1 - p) or a[0]
