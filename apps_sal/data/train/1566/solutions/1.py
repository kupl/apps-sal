def union(a, b):
    fa = find(a)
    fb = find(b)
    if rank[fa] > rank[fb]:
        dsu[fb] = fa
    elif rank[fb] > rank[fa]:
        dsu[fa] = fb
    else:
        rank[fa] += 1
        dsu[fb] = fa


def find(x):
    while x != dsu[x]:
        dsu[x] = dsu[dsu[x]]
        x = dsu[x]
    return x


for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    dsu = [i for i in range(n)]
    rank = [0] * n
    ones = []
    zeros = []
    for i in range(q):
        a, b, c = list(map(int, input().split()))
        if c == 1:
            ones.append([a - 1, b - 1])
        else:
            zeros.append([a - 1, b - 1])
    flag = 0
    for i in zeros:
        f1 = find(i[0])
        f2 = find(i[1])
        union(i[0], i[1])
    color = [0] * n
    for i in ones:
        f1 = find(i[0])
        f2 = find(i[1])
        if f1 == f2:
            flag = 1
        else:
            if color[f1] == 0 and color[f2] == 0:
                color[f1] = -1
                color[f2] = 1
            elif color[f1] != 0 and color[f2] == 0:
                color[f2] = -color[f1]
            elif color[f2] != 0 and color[f1] == 0:
                color[f1] = -color[f2]
            elif color[f2] == color[f1]:
                flag = 1

    print("yes" if flag == 0 else "no")
