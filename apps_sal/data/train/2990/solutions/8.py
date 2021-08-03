def monty_hall(correct, guess):
    return int(round((sum(1 for i in guess if i != correct)) / len(guess), 2) * 100)
