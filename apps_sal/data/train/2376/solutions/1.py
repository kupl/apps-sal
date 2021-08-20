import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, k) = map(int, input().split())
    neig = [0] * n
    for i in range(n):
        neig[i] = [0]
    for i in range(n - 1):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        neig[a][0] += 1
        neig[b][0] += 1
        neig[a].append(b)
        neig[b].append(a)
    conleaves = [0] * n
    for i in range(n):
        conleaves[i] = [0]
    goodvertices = []
    mx = 0
    for i in range(n):
        if neig[i][0] == 1:
            if neig[neig[i][1]][0] > 0:
                conleaves[neig[i][1]][0] += 1
                conleaves[neig[i][1]].append(i)
                neig[i][0] = 0
                if conleaves[neig[i][1]][0] == k:
                    goodvertices.append(neig[i][1])
    while len(goodvertices) > 0:
        v = goodvertices.pop()
        rem = conleaves[v][0] // k
        mx += rem
        rest = conleaves[v][0] % k
        conleaves[v] = conleaves[v][0:rest + 1]
        conleaves[v][0] = rest
        neig[v][0] -= rem * k
        if neig[v][0] == 1:
            for i in range(1, len(neig[v])):
                if neig[neig[v][i]][0] > 0:
                    neig[v][0] = 0
                    conleaves[neig[v][i]][0] += 1
                    conleaves[neig[v][i]].append(v)
                    if conleaves[neig[v][i]][0] == k:
                        goodvertices.append(neig[v][i])
    print(mx)
