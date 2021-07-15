def remove_duplicate_words(s):
    nlist = []
    for i in s.split():
        if i not in nlist:
            nlist.append(i)
    return ' '.join(nlist)
