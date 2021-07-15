def vowel_indices(word):
    vowels = frozenset(('A','E','I','O','U','Y','a','e','i','o','u','y'));
    idx_list = []
    for idx, letter in enumerate(word):
        if (letter in vowels):
            idx_list.append(idx+1)
    return idx_list
