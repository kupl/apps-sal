def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    return [i for i, l in enumerate(word, start=1) if l in vowels]
