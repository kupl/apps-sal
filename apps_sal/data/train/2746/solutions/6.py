def check_vowel(s, i):
    return s[i].lower() in 'aeiou' if len(s) > i > -1 else False
