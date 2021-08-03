import sys
sys.setrecursionlimit(10**9)
def read(): return sys.stdin.readline()


def read_ints():
    return list(map(int, read().split()))


def read_intgrid(h):
    return list(list(map(int, read().split()))for i in range(h))


def read_strgrid(h):
    return list(list(read())for i in range(h))


def main():
    # input data
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append((b, c))
        G[b].append((a, c))

    # solve
    # dfsで全域木を走査していく。親ノードと辺のラベルが同じならそれ以外のものを、異なるならラベルを頂点に振っていく

    vis = [0] * n
    label = [-1] * n
    label[0] = 1

    def dfs(v):
        vis[v] = 1
        for x, c in G[v]:
            if vis[x]:
                continue
            # print(x,c,label)
            if label[x] == -1:
                if label[v] == c:
                    if label[v] == 1:
                        label[x] = label[v] + 1
                    else:
                        label[x] = label[v] - 1
                else:
                    label[x] = c
            dfs(x)
    dfs(0)
    print('\n'.join(map(str, label)))
    return None


def __starting_point():
    main()


__starting_point()
