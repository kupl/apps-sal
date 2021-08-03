import math
for _ in range(int(input())):
    n = int(input())
    xs = list(map(int, input().split()))
    p, q = map(int, input().split())
    angles = sorted(math.atan((x - p) / q) for x in xs)
    print(sum(angles[n // 2:]) - sum(angles[:n // 2]))
