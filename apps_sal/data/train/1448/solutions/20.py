# cook your dish here
for _ in range(int(input())):
    (a, d, k, n, inc) = map(int, input().split())

    ans = a - d
    for i in range(1, n + 1):
        ans += d
        if i % k == 0:
            d += inc

    print(ans)
