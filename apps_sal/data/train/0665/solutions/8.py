for i in range(int(input())):
    n, m = map(int, input().split())
    ratings = list(map(int, input().split()))
    ratings_after = [[] for _ in range(m)]
    max_rating_months = []

    for i in range(n):
        curr_changes = list(map(int, input().split()))
        best_rating = ratings[i] + curr_changes[0]
        curr_r, rat_month = best_rating, 0

        ratings_after[0].append(curr_r)
        for k in range(1, m):
            curr_r += curr_changes[k]

            if curr_changes[k] > 0:
                if curr_r > best_rating:
                    best_rating = curr_r
                    rat_month = k

            ratings_after[k].append(curr_r)
        max_rating_months.append(rat_month)

    rankings = [[] for _ in range(n)]

    for x in range(m):
        month = ratings_after[x]
        new_mon = sorted(month, reverse=True)

        for y in range(n):
            rankings[y].append(new_mon.index(month[y]))

    index, counter = 0, 0

    for player in rankings:
        best = player.index(min(player))

        if best != max_rating_months[index]:
            counter += 1
        index += 1

    print(counter)
