def count_correct_characters(correct, guess):
    if len(correct) != len(guess): raise Exception
    return sum(a == b for a,b in zip(correct, guess))

