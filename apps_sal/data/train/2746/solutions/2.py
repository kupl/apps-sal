def check_vowel(string, position):
    if position < 0:
        return False
    try:
        return string[position].lower() in ['a', 'e', 'i', 'o', 'u']
    except IndexError:
        return False
