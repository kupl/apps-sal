def main():
    n, m = map(int, input().split())
    G = [-1] * n
    Node = {}
    for i in range(n):
        Node[i + 1] = []
    for i in range(m):
        u, v, c = map(int, input().split())
        Node[u] += [[v, c]]
        Node[v] += [[u, c]]
    que = [0]
    G[0] = 1
    while len(que) > 0:
        q = que.pop(0)
        for nv, w in Node[q + 1]:
            if G[nv - 1] != -1:
                continue
            if G[q] == w:
                G[nv - 1] = (G[q] + 1) % n
            else:
                G[nv - 1] = w
            que.append(nv - 1)
    cnt = 0
    for i in range(n):
        if G[i] == -1:
            cnt += 1
    if cnt > 0:
        print('No')
        return
    for i in range(n):
        print(G[i])


def __starting_point():
    main()


__starting_point()
