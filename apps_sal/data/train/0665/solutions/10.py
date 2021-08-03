for _ in range(int(input())):
    n, m = map(int, input().split())
    rating = list(map(int, input().split()))
    track = [[] for i in range(n)]
    cng = []
    for i in range(n):
        cng.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(n):
            rating[j] += cng[j][i]
        x = sorted(enumerate(rating), key=lambda x: x[1], reverse=True)
        r = 1
        if i != 0:
            if x[0][1] > track[x[0][0]][0] or r < track[x[0][0]][1]:
                if x[0][1] > track[x[0][0]][0] and r < track[x[0][0]][1]:
                    track[x[0][0]][2] = False
                else:
                    track[x[0][0]][2] = True
                if x[0][1] > track[x[0][0]][0]:
                    track[x[0][0]][0] = x[0][1]
                if r < track[x[0][0]][1]:
                    track[x[0][0]][1] = r
            for k in range(1, n):
                if x[k][1] != x[k - 1][1]:
                    r = k + 1
                if x[k][1] > track[x[k][0]][0] or r < track[x[k][0]][1]:
                    if x[k][1] > track[x[k][0]][0] and r < track[x[k][0]][1]:
                        track[x[k][0]][2] = False
                    else:
                        track[x[k][0]][2] = True
                    if x[k][1] > track[x[k][0]][0]:
                        track[x[k][0]][0] = x[k][1]
                    if r < track[x[k][0]][1]:
                        track[x[k][0]][1] = r
        else:
            track[x[0][0]].append(x[0][1])
            track[x[0][0]].append(1)
            track[x[0][0]].append(False)
            for k in range(1, n):
                if x[k][1] != x[k - 1][1]:
                    r = k + 1
                track[x[k][0]].append(x[k][1])
                track[x[k][0]].append(r)
                track[x[k][0]].append(False)

    out = 0
    for i in track:
        if i[2]:
            out += 1
    print(out)
