def is_alt(s):
    vowels = 'aeiou'
    prev = s[0]
    for ch in s[1:]:
        if prev in vowels and ch in vowels or (prev not in vowels and ch not in vowels):
            return False
        prev = ch
    return True
