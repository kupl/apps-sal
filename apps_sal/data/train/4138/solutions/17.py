def count_correct_characters(correct, guess):
    if len(correct)!=len(guess):
        raise ValueError
    else:
        return sum(1 for x,y in zip(correct, guess) if x==y)
