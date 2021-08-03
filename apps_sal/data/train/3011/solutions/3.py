from statistics import mean


def learn_charitable_game(arr):
    return not mean(arr) % 1 and any(arr)
