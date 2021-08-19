def check_vowel(s, pos):
    return 0 <= pos < len(s) and s.lower()[pos] in 'aeiou'
