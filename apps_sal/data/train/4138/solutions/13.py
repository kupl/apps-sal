def count_correct_characters(correct, guess):
    num = 0
    if len(correct) != len(guess):
        raise Exception('The lengths are not the same')
    for n in range(len(correct)):
        if list(correct)[n] == list(guess)[n]:
            num += 1
    return num
