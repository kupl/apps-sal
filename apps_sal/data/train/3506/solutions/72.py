def vowel_indices(word):
    output = []
    for i in range(0, len(word)):
        if word[i] in 'aeiouyAEIOUY':
            output.append(i + 1)
    return output
