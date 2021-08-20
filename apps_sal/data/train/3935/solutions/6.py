vowels = 'aeiou'


def vowel_recognition(stg):
    l = len(stg)
    return sum(((i + 1) * (l - i) for (i, c) in enumerate(stg.lower()) if c in vowels))
