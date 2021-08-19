pattern = lambda n, a=1, *ignored: '\n'.join([s + s[1:] * (a - 1) for s in (lambda u: u(list((u(' ' * (i - 1) + str(i % 10) + ' ' * (n - i)) for i in range(1, n + 1)))))(lambda x: x + x[-2::-1])])
