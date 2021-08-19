from collections import *
t = 1
while t:
    t -= 1
    n = int(input())
    dis = [0 for i in range(1000001)]
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        x += 500000
        y += 500000
        dis[x] += 1
        if y == 1000000:
            continue
        else:
            dis[y + 1] -= 1
    for i in range(1, len(dis)):
        dis[i] += dis[i - 1]
    print(sum(dis) % 1000000007)
