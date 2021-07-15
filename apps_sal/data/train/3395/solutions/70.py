def remove_duplicate_words(s):
    s1 = []
    [s1.append(x) for x in s.split() if x not in s1]
    return ' '.join(s1)
