def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [i + 1 for i in range(0, len(word)) if word[i].lower() in vowels]
