def __starting_point():
    for i in range(int(input())):
        (n, q) = list(map(int, input().split()))
        res = q * (n + q + 1) / (q + 1)
        print(f'{res:.10f}')


__starting_point()
