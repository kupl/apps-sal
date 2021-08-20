def absent_vowel(x):
    VOWELS = set('aeiou')
    INDEX = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    missing = VOWELS.difference(set(x.lower()))
    return INDEX.get(''.join(missing))
