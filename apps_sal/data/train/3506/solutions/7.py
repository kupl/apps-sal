def vowel_indices(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lst = []
    for index in range(len(word)):
        if word[index] in vowels:
            lst.append(index + 1)
    return lst
