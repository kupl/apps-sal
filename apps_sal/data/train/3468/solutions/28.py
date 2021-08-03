def scramble(str, wrd):
    w = set(wrd)
    for i in w:
        if str.count(i) < wrd.count(i):
            return False
    return True
