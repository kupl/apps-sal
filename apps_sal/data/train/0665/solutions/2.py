def check(rat, rank_mont):
    c = 0
    for i in range(len(rank_mont)):
        if(rat[i] != rank_mont[i]):
            c += 1
    return c


def ranking(rat, rank_min, mont, n, m):
    rat_sort = []

    for i in range(m):
        rat_sort.append(sorted(rat[i], reverse=True, key=lambda x: x[0]))

    for i in range(m):
        r, j = 1, 0
        while(j < n):
            key = rat_sort[i][j][0]
            c = 0
            while(j < n):
                if(key == rat_sort[i][j][0]):
                    if(rank_min[rat_sort[i][j][1] - 1] > r):
                        rank_min[rat_sort[i][j][1] - 1] = r
                        mont[rat_sort[i][j][1] - 1] = i + 1
                    c += 1
                else:
                    break
                j += 1
            r += c


for T in range(int(input())):
    n, m = list(map(int, input().split()))
    initial_rating = list(map(int, input().split()))
    rat = [list(map(int, input().split())) for i in range(n)]

    rat_player, m_rat_player = [], []
    for i in range(n):
        m_rat, x = 0, []
        for j in range(m):
            x.append(initial_rating[i] + rat[i][j])
            initial_rating[i] = x[j]
            if(m_rat < x[j]):
                m_rat = x[j]
                month = j + 1
        rat_player.append(x)
        m_rat_player.append(month)

    rat_month = []
    for i in range(m):
        x = []
        for j in range(n):
            x.append([rat_player[j][i], j + 1])
        rat_month.append(x)

    rank_min, mont = [501] * (n), [0] * (n)

    ranking(rat_month, rank_min, mont, n, m)

    count = check(m_rat_player, mont)

    print(count)
