def absent_vowel(x):
    strings = ['a', 'e', 'i', 'o', 'u']
    for i in strings:
        if i not in x:
            return strings.index(i)
