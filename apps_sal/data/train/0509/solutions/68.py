from collections import defaultdict, deque

n, m = map(int, input().split())
G = defaultdict(list)

for _ in range(m):
    i, j, w = map(int, input().split())
    G[i].append((j, w))
    G[j].append((i, w))

ans = [0] * (n + 1)
ans[1] = 1
q = deque([1])

while q:
    node = q.popleft()
    for nei, w in G[node]:
        if ans[nei]:
            continue
        # 現在のノードに書き込まれた数と、辺の数字が一致
        if ans[node] == w:
            # 異なる数字を次のノードに入れる
            ans[nei] = w + 1 if w < n else 1
        # 現在のノードに書き込まれた数と、辺の数字が不一致
        else:
            ans[nei] = w
        q.append(nei)

for i in range(n):
    print(ans[i + 1])
