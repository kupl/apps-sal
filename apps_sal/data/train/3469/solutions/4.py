CONSONANTS = set('bcdfghjklmnpqrstvwxyz')


def count_consonants(text):
    return len(CONSONANTS & set(text.lower()))
