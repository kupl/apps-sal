# cook your dish here
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    r = list(map(int, input().split()))
    rating = [[r[i]] * (m) for i in range(n)]
    ranking = [[0] * m for i in range(n)]
    for i in range(n):
        diff = list(map(int, input().split()))
        for j in range(m):
            rating[i][j] += diff[j]
            if j + 1 < m:
                rating[i][j + 1] = rating[i][j]

    for i in range(m):
        rate = [[j, rating[j][i]] for j in range(n)]
        rate = sorted(rate, key=lambda x: x[1], reverse=True)
        c = 1
        gap = 0
        for j in range(n):
            if j > 0 and rate[j - 1][1] == rate[j][1]:
                gap += 1
            if j > 0 and rate[j - 1][1] != rate[j][1]:
                c += 1 + gap
                gap = 0
            ranking[rate[j][0]][i] = c

    count = 0
    for i in range(n):
        rate = rating[i].copy()
        i1 = rate.index(max(rate))
        rank = ranking[i].copy()
        i2 = rank.index(min(rank))
        if i1 != i2:
            count += 1
    print(count)
