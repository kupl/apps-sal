def count_consonants(s):
    return len(set((c for c in s.lower() if c in 'bcdfghjklmnpqrstvwxyz')))
