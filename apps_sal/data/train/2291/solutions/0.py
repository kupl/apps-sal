from collections import defaultdict
N = int(input())
C = defaultdict(int)
for i in range(N):
    D = int(input())
    C[D] = i + 1
E = []
H = [1] * (N + 1)
DD = sorted([[k, v] for k, v in C.items()], reverse=True)
Adj = [[] for i in range(N)]
for D, n in DD[:-1]:
    try:
        p = C[D - N + 2 * H[n]]
        if n == p:
            raise Error
        E.append([n, p])
        Adj[n - 1].append(p - 1)
        Adj[p - 1].append(n - 1)
        H[p] += H[n]
    except:
        print(-1)
        break
else:
    dist = [N] * N
    dist[DD[-1][1] - 1] = 0
    Q = [DD[-1][1] - 1] + [N] * N
    tail = 1
    for i in range(N):
        s = Q[i]
        if s == N:
            print(-1)
            break
        for adj in Adj[s]:
            if dist[adj] == N:
                dist[adj] = dist[s] + 1
                Q[tail] = adj
                tail += 1
    else:
        if sum(dist) == DD[-1][0]:
            for e in E:
                print(e[0], e[1])
        else:
            print(-1)
