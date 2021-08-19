T = int(input())
for _ in range(T):
    a = int(input())
    hh = sorted(map(int, input().split()))
    ans = 10 ** 10
    for (h1, h2) in zip(hh[:-1], hh[1:]):
        ans = min(ans, h2 - h1)
    print(ans)
