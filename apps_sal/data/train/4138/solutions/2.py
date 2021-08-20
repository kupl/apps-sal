def count_correct_characters(correct, guess):
    if len(correct) == len(guess):
        return sum((1 for (cc, cg) in zip(correct, guess) if cc == cg))
    else:
        raise Exception
