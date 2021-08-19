from collections import deque
(n, d) = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
ans = 0
D = deque()
for i in range(n):
    D.append(x[i])
    if D[-1] - D[0] <= d and len(D) >= 3:
        ans += (len(D) - 1) * (len(D) - 2) // 2
    while D[-1] - D[0] > d:
        D.popleft()
        if D[-1] - D[0] <= d:
            ans += (len(D) - 1) * (len(D) - 2) // 2
print(ans)
