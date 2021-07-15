def vowel_indices(word):
    word = word.lower()
    indexes = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in range(0, len(word)):
        if word[i] in vowels:
            indexes.append(i + 1)
    return indexes
    # your code here

