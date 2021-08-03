N = int(input())
S = 0
minB = 1000000000000000000
for _ in range(N):
    x, y = list(map(int, input().split()))
    S += x
    if x > y:
        minB = min(minB, y)

print((max(0, S - minB)))
