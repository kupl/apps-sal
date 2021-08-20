def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [x + 1 for (x, y) in enumerate(word) if y.lower() in vowels]
