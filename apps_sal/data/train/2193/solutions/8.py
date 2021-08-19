n = int(input())
ans = 1
(a, b, c, d) = map(int, input().split())
s = a + b + c + d
for i in range(n - 1):
    (a, b, c, d) = map(int, input().split())
    t = a + b + c + d
    if s < t:
        ans += 1
print(ans)
