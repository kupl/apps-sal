def consonant_count(s):
    return sum(c in "bcdfghjklmnpqrstvwxyz" for c in s.lower())
