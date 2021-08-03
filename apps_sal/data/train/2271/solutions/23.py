import sys
from collections import deque

input = sys.stdin.readline


def bfs(N, G, p):
    # Connected compoponent
    c_comp_p_list = []
    c_comp_i_list = []
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        c_comp_p_list.append([p[i]])
        c_comp_i_list.append(set([i + 1]))
        cc_p_add = c_comp_p_list[-1].append
        cc_i_add = c_comp_i_list[-1].add

        queue = deque(G[i])
        while queue:
            u = queue.popleft()
            if visited[u]:
                continue
            visited[u] = True
            cc_p_add(p[u])
            cc_i_add(u + 1)

            for v in G[u]:
                if visited[v]:
                    continue
                queue.append(v)

    res = 0
    for c_comp_p, c_comp_i in zip(c_comp_p_list, c_comp_i_list):
        for pp in c_comp_p:
            if pp in c_comp_i:
                res += 1
    return res


def main():
    N, M = list(map(int, input().split()))
    p = tuple(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = list(map(int, input().split()))
        x -= 1
        y -= 1
        G[x].append(y)
        G[y].append(x)

    ans = bfs(N, G, p)
    print(ans)


def __starting_point():
    main()


__starting_point()
