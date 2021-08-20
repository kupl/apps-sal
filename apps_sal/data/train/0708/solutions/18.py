for _ in range(int(input())):
    (n, a) = map(int, input().split())
    m = 10 ** 9 + 7
    p = 1
    f = 0
    l = a
    prev = 1
    for i in range(1, n + 1):
        a = l * prev
        p = pow(a, 2 * i - 1, m)
        prev = prev * p % m
        f = (f + p) % m
    print(f % m)
