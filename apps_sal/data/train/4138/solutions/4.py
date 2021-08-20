def count_correct_characters(correct, guess):
    if len(correct) == len(guess):
        return sum((c == g for (c, g) in zip(correct, guess)))
    else:
        raise Exception('guess contains the wrong number of characters')
