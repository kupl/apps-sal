def vowel_indices(word):
    word = word.lower()
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'y']
    new_lst = []
    for index in range(len(word)):
        if word[index] in vowel_lst:
            new_lst.append(index + 1)
    return new_lst
