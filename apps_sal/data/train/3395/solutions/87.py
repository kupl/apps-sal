def remove_duplicate_words(s):
    nwrd = []
    for i in s.split(' '):
        if i in nwrd:
            pass
        else:
            nwrd.append(i)
    return " ".join(nwrd)
