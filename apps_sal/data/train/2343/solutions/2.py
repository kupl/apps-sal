t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    a = []
    i = 0
    while d > (1 << (i + 1)) - 1:
        a.append(1 << i)
        i += 1
    a.append((1 << i) - (1 << (i + 1)) + d + 1)
    # print(a)
    ans = 1
    for x in a:
        ans *= x + 1
        ans %= m
    print((ans - 1) % m)
