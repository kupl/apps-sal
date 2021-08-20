def remove_duplicate_words(s):
    new = ''
    sSplit = s.split(' ')
    print(sSplit)
    for i in sSplit:
        if i not in new:
            new += i + ' '
    return new.rstrip()
