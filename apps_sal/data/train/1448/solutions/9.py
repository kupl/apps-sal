T = int(input())
for i in range(T):
    (a, d, k, n, inc) = list(map(int, input().split()))
    for i in range(1, n + 1):
        if i == 1:
            a = a
        elif i % k != 0:
            a += d
        else:
            a += d
            d += inc
    print(a)
