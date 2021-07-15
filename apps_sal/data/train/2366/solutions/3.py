t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = 10 ** 9
    ans = 0
    for x in reversed(a):
        if x > mn:
            ans += 1
        mn = min(mn, x)
    print(ans)
