from sys import stdin
input = stdin.readline
q = int(input())
for query in range(q):
    n, m = map(int, input().split())
    dupa = [0] * (3 * n + 1)
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        if dupa[u] == 0 and dupa[v] == 0:
            dupa[u] = 1
            dupa[v] = 1
            if len(edges) < n:
                edges.append(i + 1)
    if len(edges) == n:
        print("Matching")
        print(*edges)
    else:
        print("IndSet")
        chuj = 0
        for i in range(1, 3 * n + 1):
            if chuj == n:
                break
            if dupa[i] == 0:
                if chuj < n - 1:
                    print(i, end=" ")
                else:
                    print(i)
                chuj += 1
