
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = max(a) - min(a)
    for i in range(1, n):
        ans = min(a[i] - a[i - 1], ans)
    print(ans)
