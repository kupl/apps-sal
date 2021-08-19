def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception()
    return sum((l1 == l2 for (l1, l2) in zip(correct, guess)))
