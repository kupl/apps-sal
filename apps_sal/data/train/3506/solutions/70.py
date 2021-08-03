def vowel_indices(word):
    # your code here
    li = []
    vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]
    for i in range(len(word)):
        for j in range(len(vowel)):
            if word[i] == vowel[j]:
                li.append(i + 1)
    return li
