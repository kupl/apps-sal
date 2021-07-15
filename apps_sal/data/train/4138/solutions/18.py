def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception()
    count = 0
    for i in range(len(guess)):
        if correct[i] == guess[i]:
            count += 1
    return count
