from collections import Counter

def consonant_count(str):
    return sum(c for x, c in Counter(str.lower()).items() if x in 'bcdfghjklmnpqrstvwxyz')
