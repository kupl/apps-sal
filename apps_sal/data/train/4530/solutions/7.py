def consonant_count(s):
    return sum([1 for c in s if c not in 'aeiou' and c.isalpha()])
