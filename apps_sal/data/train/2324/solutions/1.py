from collections import defaultdict, deque
N = int(input())
branch = defaultdict(set)
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    branch[a] |= {b}
    branch[b] |= {a}
check = {0}
bef = [-2] * N
bef[0] = -1
dist = [float('inf')] * N
dist[0] = 0
while len(check) > 0:
    now = check.pop()
    for nex in branch[now]:
        if bef[nex] == -2:
            bef[nex] = now
            check |= {nex}
            dist[nex] = dist[now] + 1
NG = set()
OK = {0}
now = N - 1
checked = {0}
for i in range((1 + dist[N - 1]) // 2):
    NG |= {now}
    now = bef[now]
checked |= NG
for i in range(N):
    if i in checked:
        continue
    else:
        visited = {i}
        now = i
        while True:
            now = bef[now]
            visited |= {now}
            if now in NG:
                NG |= visited
                checked |= visited
                break
            elif now in OK:
                OK |= visited
                checked |= visited
                break
if len(OK) > N // 2:
    print("Fennec")
else:
    print("Snuke")
