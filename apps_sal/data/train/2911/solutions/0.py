def count_vowels(s = ''):
    return sum(x.lower() in 'aeoui' for x in s) if type(s) == str else None
