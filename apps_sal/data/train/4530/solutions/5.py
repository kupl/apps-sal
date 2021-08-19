def consonant_count(s):
    return sum((1 for x in s.lower() if x.isalpha() and x not in 'aeiou'))
