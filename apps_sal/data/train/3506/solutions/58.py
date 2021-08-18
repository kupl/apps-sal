def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [i for i, x in enumerate(word.lower(), start=1) if x in vowels]


print((vowel_indices("Apple")))
