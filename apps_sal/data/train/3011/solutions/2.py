from statistics import mean


def learn_charitable_game(arr):
    m = mean(arr)
    return int(m) == m and m > 0
