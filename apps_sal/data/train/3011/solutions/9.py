def learn_charitable_game(arr):
    return sum(arr) / len(arr) == sum(arr) // len(arr) if sum(arr) > 0 else False
