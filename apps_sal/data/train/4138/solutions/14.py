def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception()
    return sum((c == g for (c, g) in zip(correct, guess)))
