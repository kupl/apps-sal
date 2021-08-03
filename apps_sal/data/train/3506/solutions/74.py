def vowel_indices(word):
    lst = [i + 1 for i in range(0, len(word)) if word[i] in 'aeiouyAEIOUY']
    return lst
