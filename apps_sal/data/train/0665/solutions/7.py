def __starting_point():
    t = int(input())
    while t > 0:
        (N, M) = map(int, input().split())
        R = list(map(int, input().split()))
        Ratings = []
        Rankings = [[float('inf') for i in range(M)] for j in range(N)]
        for i in range(N):
            temp_ratings = list(map(int, input().split()))
            temp = []
            initial_rating = R[i]
            for rate in temp_ratings:
                temp.append(initial_rating + rate)
                initial_rating += rate
            Ratings.append(temp)
        for i in range(M):
            temp = []
            for j in range(N):
                temp.append(Ratings[j][i])
            temp = sorted(temp, reverse=True)
            dic = {}
            for j in range(N):
                if temp[j] not in dic:
                    dic[temp[j]] = j + 1
            for j in range(N):
                Rankings[j][i] = dic[Ratings[j][i]]
        cnt = 0
        for i in range(N):
            best_rating = 0
            best_rating_index = -1
            best_ranking = float('inf')
            best_ranking_index = -1
            for j in range(M):
                if Ratings[i][j] > best_rating:
                    best_rating = Ratings[i][j]
                    best_rating_index = j
                if Rankings[i][j] < best_ranking:
                    best_ranking = Rankings[i][j]
                    best_ranking_index = j
            if best_rating_index != best_ranking_index:
                cnt += 1
        print(cnt)
        t -= 1


__starting_point()
