def remove_duplicate_words(s):
    a = []
    c = s.split(' ')
    for i in c:
        if i not in a:
            a.append(i)
    return ' '.join(a)
