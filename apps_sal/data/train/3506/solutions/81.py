def vowel_indices(word):
    location = []
    for letter in range(len(word)):
        if word[letter] in "aeiouyAEIOUY":
            location.append(letter + 1)
    return location

