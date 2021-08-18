from collections import deque
N = int(input())
Ball = deque([])
m, M = float("inf"), 0
for i in range(N):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    if a < m:
        m = a
        mp = i
    if b > M:
        M = b
        Mp = i
    Ball.append((a, b))
s = max([a[0] for a in Ball])
t = min([a[1] for a in Ball])
ans = (s - m) * (M - t)
if mp == Mp:
    print(ans)
    return
l = min(Ball[mp][1], Ball[Mp][0])
r = max(Ball[mp][1], Ball[Mp][0])
for i in range(2 * N):
    if Ball:
        a, b = Ball.popleft()
        if l <= a <= r or l <= b <= r:
            pass
        elif a > r:
            r = a
        elif b < l:
            l = b
        elif a < l and b > r:
            Ball.append((a, b))
    else:
        break
if Ball:
    Ball = sorted(list(Ball), key=lambda x: (x[0], -x[1]))
    Max = [r]
    for i in range(len(Ball)):
        Max.append(max(Max[-1], Ball[i][1]))
    for i in range(len(Ball)):
        ans = min(ans, (M - m) * (Max[i] - Ball[i][0]))
    ans = min(ans, (M - m) * (Max[len(Ball)] - l))
else:
    ans = min(ans, (M - m) * (r - l))
print(ans)
