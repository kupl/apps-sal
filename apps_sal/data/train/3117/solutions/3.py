def solve(s):
    vowels = 'aeiou'
    max_len = 0
    tmp_len = 0
    prev_vowel = False
    for c in s:
        max_len = max(max_len, tmp_len)
        if not prev_vowel:
            tmp_len = 0
        if c in vowels:
            tmp_len += 1
        prev_vowel = c in vowels
    return max_len
