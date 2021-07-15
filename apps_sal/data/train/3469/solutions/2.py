def count_consonants(s):
    return len({c for c in s.lower() if c in 'bcdfghjklmnpqrstvwxyz'})
