from itertools import chain, permutations
colours = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]

def mastermind(game):
    possible = list(chain.from_iterable([c]*len(game.check([c]*4)) for c in colours))
    for p in permutations(possible):
        game.check(p)
