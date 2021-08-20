def check_vowel(stg, position):
    return 0 <= position < len(stg) and stg[position].lower() in 'aeiou'
