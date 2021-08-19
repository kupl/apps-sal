def count_consonants(text):
    return len(set((c for c in text.lower() if c in 'bcdfghjklmnpqrstvwxxyz')))
