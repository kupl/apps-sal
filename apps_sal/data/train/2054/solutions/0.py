def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        (u, v) = list(map(int, input().split()))
        u -= 1
        v -= 1
        edges.append((u, v))
    colors = list(map(int, input().split()))
    suspect = [(u, v) for (u, v) in edges if colors[u] != colors[v]]
    if len(suspect) == 0:
        print('YES')
        print(1)
    else:
        cands = set(suspect[0])
        for (u, v) in suspect:
            cands &= set([u, v])
        if len(cands) == 0:
            print('NO')
        else:
            print('YES')
            e = list(cands)[0]
            print(e + 1)


main()
