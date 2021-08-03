def remove_duplicate_words(s):
    no_dup = set()
    lstt = []
    for i in s.split():
        print(i)
        if i not in lstt:
            lstt.append(i)

        f = ' '.join(lstt)
    return f
