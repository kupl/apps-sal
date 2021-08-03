def update(c):
    if c == "Red":
        return "Blue"
    if c == "Blue":
        return "Green"
    if c == "Green":
        return "Orange"
    if c == "Orange":
        return "Purple"
    if c == "Purple":
        return "Yellow"


def mastermind(game):
    guess, I = ["Red", "Red", "Red", "Red"], 0
    while I < 4:
        answer = game.check(guess)
        if len(answer) == I:
            guess[I] = update(guess[I])
        else:
            I += 1
