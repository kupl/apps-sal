import sys

p = []
path = [0 for i in range(10**5 + 1)]


def main():

    sys.setrecursionlimit(1000000)

    N = int(input())

    e = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        e[a].append(b)
        e[b].append(a)

    col = [-1 for i in range(N)]
    col[0] = 0

    # def dfs(n,c,path):
    def dfs(n, c):
        nonlocal p
        #path =  path  + [n]
        # path.append(n)
        # print(path)
        if n == N - 1:
            p = path
        path[c] = n
        for v in e[n]:
            if col[v] == -1:
                col[v] = c + 1
                dfs(v, c + 1)
                # dfs(v,c+1,path)
                if p:
                    return
    dfs(0, 0)
    # print(p[:N+10])
    # dfs(0,0,[])

    t = col[N - 1] + 1
    if t % 2 == 0:
        sn = p[t // 2]
    else:
        sn = p[t // 2 + 1]

    colfn = [-1 for i in range(N)]
    colfn[0] = 0

    def dfs2(n, c):

        for v in e[n]:
            if v == sn:
                continue
            elif colfn[v] == -1:
                colfn[v] = c + 1
                dfs2(v, c + 1)

    dfs2(0, 0)

    fennec = -1
    for i in range(N):
        if colfn[i] != -1:
            fennec += 1

    snuke = N - fennec - 2
    if fennec > snuke:
        print("Fennec")
    else:
        print("Snuke")


def __starting_point():
    main()


__starting_point()
