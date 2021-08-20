def vowel_indices(word):
    word = word.lower()
    vowels_lst = ['a', 'e', 'i', 'o', 'u', 'y']
    index_lst = []
    for i in range(len(word)):
        if word[i] in vowels_lst:
            index_lst.append(i + 1)
    return index_lst
