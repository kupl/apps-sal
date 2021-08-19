def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))
