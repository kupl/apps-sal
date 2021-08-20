def count_correct_characters(correct, guess):
    assert len(correct) == len(guess)
    return len([a for (a, b) in zip(correct, guess) if a == b])
