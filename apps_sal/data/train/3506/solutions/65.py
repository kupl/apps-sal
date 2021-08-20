def vowel_indices(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    a = len(word)
    n = []
    for i in range(a):
        if word[i] in vowels:
            n.append(i + 1)
    return n
