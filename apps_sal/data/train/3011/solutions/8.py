def learn_charitable_game(arr):
    return set(arr) != {0} and not sum(arr) % len(arr)
