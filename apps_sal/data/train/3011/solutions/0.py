def learn_charitable_game(arr):
    return sum(arr) % len(arr) == 0 and sum(arr) > 0
