def monty_hall(correct, guesses):
    return round(sum([correct != x for x in guesses]) / len(guesses) * 100)
