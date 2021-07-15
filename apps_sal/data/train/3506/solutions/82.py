def vowel_indices(word):
    word = word.casefold()
    found = 'aeiouy'
    return [i+1 for i in range(len(word)) if word[i] in found]
