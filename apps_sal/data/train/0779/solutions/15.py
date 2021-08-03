t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    ans = l[0]
    for i in range(1, n):
        ans = (ans + l[i]) / 2
    print(ans)
