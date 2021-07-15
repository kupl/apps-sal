def remove_duplicate_words(s):
    no_dup = []
    no_dup1 = []
    for c in s.split(' '):
        if c not in no_dup:
            no_dup.append(c)
        else:
            no_dup1.append(c)
    return ' '.join(no_dup)
