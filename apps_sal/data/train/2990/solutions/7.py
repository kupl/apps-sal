def monty_hall(correct, guesses):
    return round(100 - 100.0 * guesses.count(correct) / len(guesses))
