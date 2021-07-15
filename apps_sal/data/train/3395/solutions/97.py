def remove_duplicate_words(s):
    return ' '.join(list({i: True for i in s.split(' ')}))
