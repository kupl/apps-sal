def solve(s):
    vowels = 'aeiou'
    s_vowels = sorted((c for c in s if c in vowels))
    s_consonants = sorted((c for c in s if c not in vowels))
    diff = len(s_vowels) - len(s_consonants)
    if diff == -1:
        out_string = s_consonants.pop(0)
        for (v, c) in zip(s_vowels, s_consonants):
            out_string += v + c
    elif diff == 0:
        out_string = ''
        for (v, c) in zip(s_vowels, s_consonants):
            out_string += v + c
    elif diff == 1:
        out_string = s_vowels.pop(0)
        for (c, v) in zip(s_consonants, s_vowels):
            out_string += c + v
    else:
        return 'failed'
    return out_string
