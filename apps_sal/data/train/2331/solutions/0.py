from sys import stdin
import itertools
input = stdin.readline


def getint():
    return int(input())


def getints():
    return list(map(int, input().split()))


def getint1():
    return list([int(x) - 1 for x in input().split()])


def getstr():
    return input()[:-1]


def solve():
    (n, a, b) = getint1()
    n += 1
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        (u, v) = getint1()
        adj[u].append(v)
        adj[v].append(u)
    max_child = [[-1] * 3 for _ in range(n)]
    stack = [(a, -1, 1)]
    while stack:
        (u, p, flag) = stack.pop()
        if p != -1 and len(adj[u]) < 2:
            max_child[u][0] = 1
            continue
        if flag == 1:
            stack.append((u, p, 0))
            for v in adj[u]:
                if v == p:
                    continue
                stack.append((v, u, 1))
        else:
            for v in adj[u]:
                if v == p:
                    continue
                len_v = max_child[v][0] + 1
                if len_v > max_child[u][0]:
                    max_child[u][2] = max_child[u][1]
                    max_child[u][1] = max_child[u][0]
                    max_child[u][0] = len_v
                elif len_v > max_child[u][1]:
                    max_child[u][2] = max_child[u][1]
                    max_child[u][1] = len_v
                elif len_v > max_child[u][2]:
                    max_child[u][2] = len_v
    body = []
    ret = [False] * n
    max_parent = [-1] * n
    stack.clear()
    stack = [(a, -1, 0)]
    while stack:
        (u, p, mxp) = stack.pop()
        if mxp >= 0:
            stack.append((u, p, -1))
            if p != -1 and len(adj[u]) < 2:
                continue
            max_parent[u] = mxp + 1
            chlen = [max_parent[u], -3]
            for v in adj[u]:
                if v == p:
                    continue
                len_v = max_child[v][0] + 1
                if len_v > chlen[0]:
                    chlen[1] = chlen[0]
                    chlen[0] = len_v
                elif len_v > chlen[1]:
                    chlen[1] = len_v
            for v in adj[u]:
                if v == p:
                    continue
                stack.append((v, u, chlen[int(max_child[v][0] + 1 == chlen[0])]))
        else:
            is_body = u == b
            if not is_body:
                for v in adj[u]:
                    if v != p and ret[v]:
                        is_body = True
                        break
            if is_body:
                body.append(u)
            ret[u] = is_body
    del ret
    ok = False
    body_len = len(body)
    can_turn = [False] * n
    for i in range(n):
        if 3 <= sum((1 for l in max_child[i] + [max_parent[i]] if l >= body_len)):
            can_turn[i] = True
            ok = True
    if not ok:
        print('NO')
        return
    treelen = [1] * body_len
    for i in range(body_len):
        cur = body[i]
        pre = -1 if i == 0 else body[i - 1]
        nxt = -1 if i + 1 == body_len else body[i + 1]
        for v in adj[cur]:
            if v == pre or v == nxt:
                continue
            treelen[i] = max(treelen[i], max_child[v][0] + 1)
            if can_turn[v]:
                can_turn[cur] = True
                continue
            stack = [(v, cur)]
            while stack and (not can_turn[cur]):
                (u, p) = stack.pop()
                for w in adj[u]:
                    if w == p:
                        continue
                    if can_turn[w]:
                        can_turn[cur] = True
                        break
                    stack.append((w, u))
            stack.clear()
    l = 0
    r = body_len - 1
    lmax = treelen[r] - 1
    rmin = body_len - treelen[l]
    ok = can_turn[body[l]] or can_turn[body[r]]
    while not ok and (l < lmax or rmin < r):
        if l < lmax:
            l += 1
            rmin = min(rmin, l + (body_len - treelen[l]))
        if rmin < r:
            r -= 1
            lmax = max(lmax, r - (body_len - treelen[r]))
        if can_turn[body[l]] or can_turn[body[r]]:
            ok = True
    print('YES' if ok else 'NO')
    return


def __starting_point():
    for _ in range(getint()):
        solve()


__starting_point()
