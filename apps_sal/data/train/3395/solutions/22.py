def remove_duplicate_words(s):
    o = []
    x = s.split()
    for y in x:
        if y not in o:
            o.append(y)
    return ' '.join(o)
