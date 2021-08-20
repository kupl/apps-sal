def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception('Wrong length')
    res = sum((1 for (a, b) in zip(correct, guess) if a == b))
    return res
