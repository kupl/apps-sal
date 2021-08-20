def vowel_indices(word):
    new_list = []
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y')
    for i in range(len(word)):
        if word[i] in vowels:
            new_list.append(i + 1)
    return new_list
