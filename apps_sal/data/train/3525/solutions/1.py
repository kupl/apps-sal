def flipping_game(num):
    return max([sum(num) + num[i: j + 1].count(0) - num[i: j + 1].count(1) for i in range(len(num)) for j in range(i, len(num))])
