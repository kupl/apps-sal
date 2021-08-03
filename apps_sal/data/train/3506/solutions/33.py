def vowel_indices(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    return [i for i, letter in enumerate(word.lower(), start=1) if letter in vowels]
