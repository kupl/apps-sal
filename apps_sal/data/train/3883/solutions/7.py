def solve(s):
    vowels = ''.join(sorted((ch for ch in s if ch in 'aeiou'))) + '_'
    consonants = ''.join(sorted((ch for ch in s if ch not in 'aeiou'))) + '_'
    if abs(len(vowels) - len(consonants)) > 1:
        return 'failed'
    if len(vowels) >= len(consonants):
        res = ''.join((v + c for (v, c) in zip(vowels, consonants)))
    else:
        res = ''.join((v + c for (v, c) in zip(consonants, vowels)))
    return res.strip('_')
