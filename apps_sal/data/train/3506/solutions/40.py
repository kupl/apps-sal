def vowel_indices(word):
    i = 0
    positions = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for letter in word:
        if letter in vowels:
            positions.append(word.index(letter, i) + 1)
        i += 1
    return positions
