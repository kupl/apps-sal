T = int(input())


def dist(z, i, j):
    return abs(z[i][0] - z[j][0]) + abs(z[i][1] - z[j][1])


for i in range(T):
    l = list(map(int, input().split()))
    n, m = l[0], l[1]
    grd = [list(map(int, input())) for i in range(n)]
    z = []
    for i, r in enumerate(grd):
        for j, v in enumerate(r):
            if v:
                z.append((i, j))

        distance = [0] * (n + m - 2)
        for i in range(len(z)):
            for j in range(i + 1, len(z)):
                d = dist(z, i, j)
                distance[d - 1] += 1

    print(*distance)
