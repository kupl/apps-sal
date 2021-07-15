def absent_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, v in enumerate(vowels):
        if v not in x.lower():
            return i

