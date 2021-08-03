n = int(input())
ans = 0
c = []
for i in range(n):
    a, b = map(int, input().split())
    ans += a
    if a > b:
        c.append(b)
if len(c):
    print(ans - min(c))
else:
    print(0)
