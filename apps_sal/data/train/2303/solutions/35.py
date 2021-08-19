# https://juppy.hatenablog.com/entry/2019/04/10/ARC061_-_E_%E3%81%99%E3%81%AC%E3%81%91%E5%90%9B%E3%81%AE%E5%9C%B0%E4%B8%8B%E9%89%84%E6%97%85%E8%A1%8C_-_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
# 参考にさせていただきました。

from collections import deque, defaultdict

chg = 10**6
n, m = map(int, input().split())
edges = defaultdict(set)
# m=0のためにdefaultdictにしておくべき
visited = defaultdict(set)
for i in range(m):
    p, q, c = map(int, input().split())
    edges[p + c * chg].add(q + c * chg)
    edges[q + c * chg].add(p + c * chg)
    edges[p].add(p + c * chg)
    edges[q].add(q + c * chg)
    edges[p + c * chg].add(p)
    edges[q + c * chg].add(q)
    visited[p] = False
    visited[q] = False
    visited[p + c * chg] = False
    visited[q + c * chg] = False

ans = float("inf")
que = deque()
# now, dist
que.append((1, 0))
# 今求めるのはendの距離だけなので、dist配列はいらない
# さらに、距離は0/1なのでheapで辺を管理する必要もなく、0なら最短確定なので先に、1ならその時点での最長なので後ろにすれば良い
while que:
    now, dist = que.popleft()
    if visited[now]:
        continue
    visited[now] = True
    if now == n:
        ans = dist
        break
    for to in edges[now]:
        # 駅→ホーム
        if now < chg and to > chg:
            que.append((to, dist + 1))
        else:
            que.appendleft((to, dist))
if ans == float("inf"):
    print(-1)
else:
    print(ans)
