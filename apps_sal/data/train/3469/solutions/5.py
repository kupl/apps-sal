def count_consonants(text):
    return len({ch for ch in text.lower() if ch in 'bcdfghjklmnpqrstvwxyz'})
