inf = 10**18
N = int(input())
balls = []
m, M = inf, -1
mp, Mp = -1, -1
for i in range(N):
    x, y = list(map(int, input().split()))
    if x > y:
        x, y = y, x
    balls.append((x, y))
    if m > x:
        mp = i
        m = x
    if M < y:
        Mp = i
        M = y
a = max(x[0] for x in balls)
b = min(x[1] for x in balls)
ans = (a - m) * (M - b)
if mp == Mp:
    print(ans)
    return
balls.sort()
a, b = balls[0][0], balls[-1][0]
ans = min(ans, (M - m) * (b - a))
k = inf
for i in range(N - 1):
    a = balls[i + 1][0]
    b = max(b, balls[i][1])
    k = min(k, balls[i][1])
    if a > k:
        ans = min(ans, (M - m) * (b - k))
        break
    ans = min(ans, (M - m) * (b - a))
b = max(b, balls[i][1])
k = min(k, balls[-1][1])
ans = min(ans, (M - m) * (b - k))
print(ans)
