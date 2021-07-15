def cup_and_balls(b, arr):
    game = [i == b for i in range(4)]
    for a, b in arr:
        game[a], game[b] = game[b], game[a]
    return game.index(True)
