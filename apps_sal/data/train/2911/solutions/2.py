def count_vowels(s=''):
    if type(s) != str:
        return None
    return len([c for c in s if c.lower() in "aeiou"])
