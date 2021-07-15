def mastermind(game):
    cols = {"Red", "Blue", "Green", "Orange", "Purple", "Yellow"}
    used = cols - set([c for c in cols if game.check([c]*4)])
    duff = (cols - used).pop()

    return [c for c in used for i in range(4) if game.check([duff] * i + [c] + [duff] *(3-i)) == ['Black']]
