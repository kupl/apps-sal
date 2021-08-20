import sys
readline = sys.stdin.readline


def dfs(s, t, Edge):
    N = len(Edge)
    used = [0] * N
    used[s] = 1
    used[t] = 1
    stack = [s]
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if not used[vf]:
                used[vf] = 1
                stack.append(vf)
    return used


T = int(readline())
Ans = [None] * T
for qu in range(T):
    (N, M, A, B) = map(int, readline().split())
    A -= 1
    B -= 1
    Edge = [[] for _ in range(N)]
    for _ in range(M):
        (a, b) = map(int, readline().split())
        a -= 1
        b -= 1
        Edge[a].append(b)
        Edge[b].append(a)
    sa = dfs(A, B, Edge)
    sb = dfs(B, A, Edge)
    ca = 0
    cb = 0
    for (fa, fb) in zip(sa, sb):
        if fa == fb:
            continue
        if fa:
            ca += 1
        elif fb:
            cb += 1
    Ans[qu] = ca * cb
print('\n'.join(map(str, Ans)))
