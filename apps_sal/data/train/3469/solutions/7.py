def count_consonants(text):
    return len(set(list(text.lower())).intersection(set(list('bcdfghjklmnpqrstvwxyz'))))
