def remove_duplicate_words(s):
    dictionary = s.split()
    dictionary = dict.fromkeys(dictionary)
    return ' '.join(dictionary)
