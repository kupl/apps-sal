def vowel_indices(word):
    l = []
    for (i, letter) in enumerate(word):
        if letter in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
            l.append(i + 1)
    return l
