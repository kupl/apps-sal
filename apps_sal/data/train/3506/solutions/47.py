def vowel_indices(word):
    word = word.lower()
    vowels = "aeiouy"
    l = []
    sum = 1
    for i in word:
        if i in vowels:
            l.append(sum)
            sum = sum + 1
        else:
            sum = sum + 1

    return l
