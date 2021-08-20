def vowel_indices(word):
    result = []
    for _ in range(len(word)):
        if word[_].lower() in 'aeiouy':
            result.append(_ + 1)
    return result
