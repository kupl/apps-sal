def vowel_indices(word):
    return [i+1 for i in range(len(word)) if word[i].lower() in ['a', 'e', 'i', 'o', 'u', 'y']]
