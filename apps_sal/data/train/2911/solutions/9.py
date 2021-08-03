def count_vowels(s=''):
    if type(s) == str:
        return sum(char in "aeiou" for char in s.lower())
