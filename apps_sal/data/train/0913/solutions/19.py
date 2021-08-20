try:
    (n, m, k) = list(map(int, input().split()))
    dist = [0] * (m + 1)
    max1 = 0
    cost = 0
    for i in range(0, k):
        (h1, u1, h2, u2) = list(map(int, input().split()))
        xo = min(h1, h2)
        x1 = max(h1, h2)
        yo = min(u1, u2)
        y1 = max(u1, u2)
        cost += 2 * (x1 - xo + (y1 - yo))
        lv = 1
        x = x1 - xo
        if yo - x // 4 > 1:
            lv = yo - x // 4
        up = m
        if x // 4 + y1 < up:
            up = x // 4 + y1
        for j in range(lv, up + 1):
            if j < yo:
                dist[j] += x - 4 * (yo - j)
            elif j >= yo and j <= y1:
                dist[j] += x
            else:
                dist[j] += x - 4 * (j - y1)
            if dist[j] > dist[max1]:
                max1 = j
    print(cost - dist[max1])
except:
    pass
