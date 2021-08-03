def remove_duplicate_words(s):
    single = []
    for x in s.split():
        if x not in single:
            single.append(x)
    return ' '.join(single)
