from collections import deque, defaultdict
import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
mod = 10 ** 7
table = defaultdict(set)
visit = defaultdict(int)
for i in range(M):
    (a, b, c) = map(int, input().split())
    table[a].add(a + c * mod)
    table[b].add(b + c * mod)
    table[a + c * mod].add(a)
    table[b + c * mod].add(b)
    table[a + c * mod].add(b + c * mod)
    table[b + c * mod].add(a + c * mod)
    visit[a] = 0
    visit[b] = 0
    visit[b + c * mod] = 0
    visit[a + c * mod] = 0
H = deque()
H.append((1, 0))
visit[1] = 1
ans = mod
while H:
    (x, cost) = H.popleft()
    visit[x] = 1
    if x == N:
        ans = min(ans, cost)
        break
    for y in table[x]:
        if visit[y] == 1:
            continue
        if x <= 10 ** 5 and mod <= y:
            H.append((y, cost + 1))
        else:
            H.appendleft((y, cost))
if ans == mod:
    print(-1)
else:
    print(ans)
