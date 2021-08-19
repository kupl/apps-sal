def vowel_indices(word):
    retval = []
    word = word.lower()
    for (counter, value) in enumerate(word):
        if value == 'a':
            retval.append(counter + 1)
        if value == 'e':
            retval.append(counter + 1)
        if value == 'i':
            retval.append(counter + 1)
        if value == 'o':
            retval.append(counter + 1)
        if value == 'u':
            retval.append(counter + 1)
        if value == 'y':
            retval.append(counter + 1)
    return retval
