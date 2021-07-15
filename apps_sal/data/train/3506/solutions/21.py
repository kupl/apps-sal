def vowel_indices(word):
    return [
        i+1 for i, letter in enumerate(word.lower())
        if letter in 'aeiouy'
    ]
