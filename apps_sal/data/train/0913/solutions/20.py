try:
    n, m, k = list(map(int, input().split()))
    xo, yo, x1, y1 = [0] * k, [0] * k, [0] * k, [0] * k
    dist = [0] * (m + 1)
    max1 = 0
    for i in range(0, k):
        h1, u1, h2, u2 = list(map(int, input().split()))
        xo[i] = min(h1, h2)
        x1[i] = max(h1, h2)
        yo[i] = min(u1, u2)
        y1[i] = max(u1, u2)
        lv = 1
        x = x1[i] - xo[i]
        if (yo[i] - x // 4) > 1:
            lv = yo[i] - x // 4
        up = m
        if (x // 4 + y1[i]) < up:
            up = x // 4 + y1[i]
        for j in range(lv, up + 1):
            if j < yo[i]:
                dist[j] += x - 4 * (yo[i] - j)
            elif j >= yo[i] and j <= y1[i]:
                dist[j] += x
            else:
                dist[j] += x - 4 * (j - y1[i])
            if dist[j] > dist[max1]:
                max1 = j
    cost = 0
    for i in range(k):
        cost += 2 * ((x1[i] - xo[i]) + (y1[i] - yo[i]))
    print(cost - dist[max1])

except:
    pass
