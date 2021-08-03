def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    result = []

    for i in range(0, len(word)):
        if word[i] in vowels:
            result.append(i + 1)

    return result
