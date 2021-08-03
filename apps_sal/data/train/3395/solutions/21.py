def remove_duplicate_words(s):
    ss = list(set(s.split()))
    ss.sort(key=s.index)
    return ' '.join(ss)
