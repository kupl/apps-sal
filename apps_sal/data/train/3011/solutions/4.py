def learn_charitable_game(arr):
    r = sum(arr)
    return r > 0 and r % len(arr) == 0
