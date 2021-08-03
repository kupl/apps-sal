def vowel_indices(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    index_list = []
    for indx, letter in enumerate(word.lower()):
        if letter in vowels:
            index_list.append(indx + 1)
    return index_list
