n = int(input())
for k in range(n):
    lst = input().split()
    N = int(lst[0])
    M = int(lst[1])
    rating = []
    rating.append(list(map(int, input().split())))
    change = [None for i in range(N)]
    for i in range(N):
        change[i] = list(map(int, input().split()))
    for i in range(1, M + 1):
        rating.append([])
        for j in range(0, N):
            rating[i].append(rating[i - 1][j] + change[j][i - 1])
    MaxRating = []
    MaxRatingMonth = []
    for j in range(N):
        MaxRating.append(rating[1][j])
        MaxRatingMonth.append(1)
        for i in range(2, M + 1):
            if rating[i][j] > MaxRating[j]:
                MaxRating[j] = rating[i][j]
                MaxRatingMonth[j] = i
    MaxRankingMonth = []
    newrating = []
    Ranking = [[None for j in range(N)] for i in range(0, M)]
    for i in range(1, M + 1):
        newrating.append(sorted(rating[i], reverse=True))
    for i in range(1, M + 1):
        for j in range(N):
            Ranking[i - 1][j] = newrating[i - 1].index(rating[i][j]) + 1
    MaxRankingMonth = []
    MaxRanking = []
    for j in range(N):
        MaxRankingMonth.append(1)
        MaxRanking.append(Ranking[0][j])
        for i in range(2, M + 1):
            if Ranking[i - 1][j] < MaxRanking[j]:
                MaxRanking[j] = Ranking[i - 1][j]
                MaxRankingMonth[j] = i
    count = 0
    for i in range(N):
        if MaxRankingMonth[i] != MaxRatingMonth[i]:
            count += 1
    print(count)
