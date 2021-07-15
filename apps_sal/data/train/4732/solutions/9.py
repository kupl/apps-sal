def absent_vowel(x): 
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        if i not in x.lower():
            return vowels.index(i) 
