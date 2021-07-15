def remove_duplicate_words(s):
    s1 = s.split()
    return ' '.join([s1[i] for i in range(len(s1)) if s1[i] not in s1[:i]])
