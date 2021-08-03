def monty_hall(door, guesses):
    return round(100.0 * (len(guesses) - guesses.count(door)) / len(guesses))
