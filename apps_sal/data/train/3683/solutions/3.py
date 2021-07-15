def letter_count(s):
    letters = {}
    for i in list(s):
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
