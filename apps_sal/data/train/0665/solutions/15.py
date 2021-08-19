def getRanking(ratingList, n, m):
    rank = []
    array2d = [[None for i in range(n)] for j in range(m)]
    for i in range(m):
        helper2d = [[None for i in range(2)] for j in range(n)]
        for j in range(n):
            helper2d[j][0] = j + 1
            helper2d[j][1] = ratingList[j][i]
        helper2d = sorted(helper2d, reverse=True, key=lambda x: x[1])
        arr = [x for x in range(1, n + 1)]
        for k in range(1, n):
            if helper2d[k][1] == helper2d[k - 1][1]:
                arr[k] = arr[k - 1]
        for l in range(n):
            array2d[i][helper2d[l][0] - 1] = arr[l]
    for l in range(n):
        minimum = float('inf')
        minimumIndex = None
        for o in range(m):
            if minimum > array2d[o][l]:
                minimum = array2d[o][l]
                minimumIndex = o + 1
        rank.append(minimumIndex)
    return rank


t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    r = list(map(int, input().split()))
    c = [None for j in range(n)]
    for i in range(n):
        c[i] = list(map(int, input().split()))
    ratingList = [None for i in range(n)]
    for i in range(n):
        temp = []
        temp.append(r[i] + c[i][0])
        for j in range(1, m):
            temp.append(temp[j - 1] + c[i][j])
        ratingList[i] = temp
    playerRatings = []
    for i in range(n):
        maximum = float('-inf')
        maximumMonth = None
        for j in range(m):
            if ratingList[i][j] > maximum:
                maximum = ratingList[i][j]
                maximumMonth = j + 1
        playerRatings.append(maximumMonth)
    playerRanking = getRanking(ratingList, n, m)
    count = 0
    for i in range(n):
        if playerRanking[i] != playerRatings[i]:
            count += 1
    print(count)
