t = int(input())
for i in range(0, t):
    ans = 0
    nm = input().split()
    (n, m) = (int(nm[0]), int(nm[1]))
    (rows, cols) = (m, n)
    a = [[(0, 0) for i in range(cols)] for j in range(rows)]
    max_rating_month = [0 for i in range(cols)]
    curr_rating = list(map(int, input().strip().split()))[:n]
    for i in range(0, n):
        line = list(map(int, input().strip().split()))[:m]
        max = 0
        for j in range(0, m):
            curr_rating[i] += line[j]
            if curr_rating[i] > max:
                max_rating_month[i] = j
                max = curr_rating[i]
            a[j][i] = (i, curr_rating[i])
    ranking = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        a[i].sort(key=lambda x: -x[1])
        rank = 1
        ranking[i][a[i][0][0]] = 1
        for j in range(1, n):
            if a[i][j - 1][1] == a[i][j][1]:
                ranking[i][a[i][j][0]] = rank
            else:
                ranking[i][a[i][j][0]] = j + 1
                rank = j + 1
    for i in range(n):
        best_rank = 501
        best_rank_month = 0
        for j in range(m):
            if ranking[j][i] < best_rank:
                best_rank = ranking[j][i]
                best_rank_month = j
        if best_rank_month != max_rating_month[i]:
            ans += 1
    print(ans)
