def vowel_indices(word):
    return [i + 1 for i in range(0, len(word)) if word.lower()[i] in 'aeiouy']
