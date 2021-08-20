def replace_exclamation(s):
    """Replace all vowels in string s with a '!'"""
    return s.translate(str.maketrans('aeiouAEIOU', '!!!!!!!!!!'))
