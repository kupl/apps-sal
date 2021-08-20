def remove_duplicate_words(s):
    s = s.split()
    m = []
    for i in s:
        if i not in m:
            m.append(i)
    return ' '.join(m)
