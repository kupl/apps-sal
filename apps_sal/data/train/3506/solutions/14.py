def vowel_indices(word):
    return([count for count, char in enumerate(word, 1) if char.lower() in ["a", "e", "i", "o", "u", "y"]])
