def remove_duplicate_words(str):
    l = str.split()
    s = []
    r = []
    for i in range(len(l)):
        if l[i] not in s:
            s.append(l[i])
            r.append(l[i])
    satr = ' '.join([elem for elem in r])
    return satr
