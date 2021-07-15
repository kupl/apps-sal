def vowel_indices(word):
    vowel = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    count = 1
    lst = []
    for letter in word:
        if letter in vowel:
            
            lst.append(count)
        count += 1
    return lst
