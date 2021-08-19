def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception
    return sum((i == j for (i, j) in zip(correct, guess)))
