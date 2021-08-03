def count_paths(N, C, f=lambda n: eval('*'.join(map(str, range(1, n + 1))))):
    a, y = C
    b = N - 1 - y
    return 1 - (b == 0)if a == 0else 1 - (a == 0)if b == 0 else f(a + b) // f(a) // f(b)
