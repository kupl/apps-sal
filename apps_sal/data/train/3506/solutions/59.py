def vowel_indices(word):
    vowels = ['a','e','i','o','u','y']
    return [i + 1 for i, c in enumerate(list(word)) if c.lower() in vowels]

