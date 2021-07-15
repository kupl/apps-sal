def consonant_count(s):
    return sum(x.lower() in 'bcdfghjklmnpqrstvwxyz' for x in s)
