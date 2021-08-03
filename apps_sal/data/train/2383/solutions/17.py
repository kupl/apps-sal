t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = min(max(a + a, b) ** 2, max(b + b, a) ** 2)
    print(ans)
