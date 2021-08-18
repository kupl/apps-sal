def count_correct_characters(correct, guess):
    print(correct, guess)
    if len(correct) != len(guess):
        return error

    a = list((correct))
    b = list((guess))
    print(a, b)
    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            c = c + 1
    return c
