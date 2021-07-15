def check_vowel(string, position):
    return 0 <= position <= len(string) and string[position] in 'aeiouAEIOU'
