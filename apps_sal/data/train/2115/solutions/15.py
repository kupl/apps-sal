from collections import deque
n, d = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

D = deque()
total = 0
s = 0

for i in range(n - 1):
    while len(D) > 0 and s + x[i + 1] - x[i] > d:
        s -= D.popleft()

    if s + x[i + 1] - x[i] <= d:
        D.append(x[i + 1] - x[i])
        total += (len(D) * (len(D) - 1)) // 2
        s += D[-1]

print(total)
