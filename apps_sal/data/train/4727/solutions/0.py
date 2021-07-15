REMOVE_VOWS = str.maketrans('','','aeiou')

def remove_vowels(s):
    return s.translate(REMOVE_VOWS)
