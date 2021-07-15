VOWELS = 'aeiouyAEIOUY'

def vowel_indices(word):
    return [i + 1 for i, l in enumerate(word) if l in VOWELS]
