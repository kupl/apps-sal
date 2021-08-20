test = int(input())
m = pow(10, 9) + 7
for _ in range(test):
    (n, a) = map(int, input().split())
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
