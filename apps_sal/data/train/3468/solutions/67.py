def scramble(s1, s2):
    import numpy
    options = {}
    for i in s1:
        if i in options:
            options[i] += 1
        else:
            options[i] = 1
    word = {}
    for i in s2:
        if i not in options:
            return False
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    for i in word:
        if word[i] > options[i]:
            return False
    return True
