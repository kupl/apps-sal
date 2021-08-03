from itertools import permutations


def mastermind(game):
    colors = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    counts = []
    good = []
    for color in colors:
        attempt = [color, color, color, color]
        answer = game.check(attempt)
        if answer == 'WON!':
            return
        for i in range(answer.count('Black')):
            good.append(color)
    for p in permutations(good):
        answer = game.check(p)
        if answer.count('Black') == 4:
            return
