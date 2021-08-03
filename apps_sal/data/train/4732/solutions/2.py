def absent_vowel(stg):
    return next(i for i, v in enumerate("aeiou") if v not in stg)
