def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma, mb = min(a), min(b)
    ans = 0
    for i in range(n):
        ans += max(a[i] - ma, b[i] - mb)
    print(ans)


t = int(input())
for _ in range(t):
    solve()
