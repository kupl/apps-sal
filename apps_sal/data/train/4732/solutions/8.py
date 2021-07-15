def absent_vowel(x): 
    dictionary = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 3,
    "u": 4}
    for vow in "aeiou":
        if vow not in x:
            return dictionary.get(vow)
