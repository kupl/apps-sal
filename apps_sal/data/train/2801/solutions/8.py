(m, r) = (lambda s: s + s[-2::-1], lambda s, n: s + s[1:] * n)
pattern = lambda n, h=1, v=1, *a: '\n'.join(r(m(list((r(m(' ' * (i - 1) + str(i % 10) + ' ' * (n - i)), h - 1) for i in range(1, n + 1)))), v - 1))
