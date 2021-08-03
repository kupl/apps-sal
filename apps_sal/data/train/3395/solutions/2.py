def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key=s.index))
