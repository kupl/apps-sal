def points(n):
    n_2 = n ** 2
    sq = [i ** 2 for i in range(1, n)]
    count = 0
    for i in sq:
        for j in sq:
            if i + j <= n_2:
                count = count + 1
    count = 4 * (count + n) + 1
    return(count)
