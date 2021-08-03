def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Error('The two lengths are not the same')
    return sum(correct[i] == guess[i] for i in range(len(correct)))
