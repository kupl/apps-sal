def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise ValueError('Error: different word lengths')
    return sum(a == b for a, b in zip(correct, guess))
