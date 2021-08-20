def remove_duplicate_words(s):
    words = set()
    stree = ''
    for word in s.split():
        if word not in words:
            stree += word + ' '
            words.add(word)
    return stree[0:-1]
