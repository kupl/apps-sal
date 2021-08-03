def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    result = [i + 1 for i, char in enumerate(word) if char in vowels]
    return result
