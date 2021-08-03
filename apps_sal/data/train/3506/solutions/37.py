def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [char + 1 for char in range(0, len(word)) if word[char].lower() in vowels]
