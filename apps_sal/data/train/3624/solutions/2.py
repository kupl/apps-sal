def distribution_of_candy(candies):
    turn = 0
    while len(set(candies)) > 1:
        candies = [(m + m%2) // 2 + (n + n%2) // 2 for m, n in zip(candies, candies[-1:] + candies[:-1])]
        turn += 1
    return [turn, candies[0]]
