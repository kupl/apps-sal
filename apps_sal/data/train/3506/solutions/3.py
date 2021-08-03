VOWELS = set("aeiuoy")


def vowel_indices(word):
    return [i for i, v in enumerate(word.lower(), 1) if v in VOWELS]
