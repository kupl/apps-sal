def remove_duplicate_words(s):
    return " ".join(list({x: 1 for x in s.split(' ')}))
