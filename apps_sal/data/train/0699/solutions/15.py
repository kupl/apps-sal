t = int(input())
for _ in range(t):
    (n, k, d) = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    contests = total // k
    if contests <= d:
        ans = contests
    else:
        ans = d
    print(ans)
