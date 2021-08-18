def fact(nnn):
    f = 1
    for i in range(1, nnn + 1):
        f = f * i
    return f


t = int(input())
for i in range(0, t):
    n = int(input())
    lis = list(map(int, input().strip().split()))[:n]
    s = sum(lis)
    st = "1" * n
    last = int(st)
    ans = fact(n - 1) * s * last
    print(ans)
