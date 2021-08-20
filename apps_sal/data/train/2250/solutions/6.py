(n, m, k) = list(map(int, input().split()))
(dm, dp) = ({}, {})
vis = {}
sensors = []
border = set()
for el in [(0, m), (n, 0), (0, 0), (n, m)]:
    border.add(el)
for _ in range(k):
    (x, y) = list(map(int, input().split()))
    if not x - y in dm:
        dm[x - y] = []
    dm[x - y].append((x, y))
    if not x + y in dp:
        dp[x + y] = []
    dp[x + y].append((x, y))
    vis[x, y] = -1
    sensors.append((x, y))
(x, y) = (0, 0)
time = 0
move = (1, 1)
while True:
    if move == (1, 1):
        v = min(n - x, m - y)
        nxt = (x + v, y + v)
        if nxt[0] == n:
            move = (-1, 1)
        else:
            move = (1, -1)
        if x - y in dm:
            for sensor in dm[x - y]:
                if vis[sensor] == -1:
                    vis[sensor] = time + sensor[0] - x
        time += v
    elif move == (-1, -1):
        v = min(x, y)
        nxt = (x - v, y - v)
        if nxt[0] == 0:
            move = (1, -1)
        else:
            move = (-1, 1)
        if x - y in dm:
            for sensor in dm[x - y]:
                if vis[sensor] == -1:
                    vis[sensor] = time + x - sensor[0]
        time += v
    elif move == (-1, 1):
        v = min(x, m - y)
        nxt = (x - v, y + v)
        if nxt[0] == 0:
            move = (1, 1)
        else:
            move = (-1, -1)
        if x + y in dp:
            for sensor in dp[x + y]:
                if vis[sensor] == -1:
                    vis[sensor] = time + x - sensor[0]
        time += v
    else:
        v = min(n - x, y)
        nxt = (x + v, y - v)
        if nxt[0] == n:
            move = (-1, -1)
        else:
            move = (1, 1)
        if x + y in dp:
            for sensor in dp[x + y]:
                if vis[sensor] == -1:
                    vis[sensor] = time + sensor[0] - x
        time += v
    if nxt in border:
        break
    else:
        border.add(nxt)
    (x, y) = nxt
for i in range(k):
    print(vis[sensors[i]])
