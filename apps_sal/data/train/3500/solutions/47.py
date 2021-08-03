def remove_exclamation_marks(s):
    sl = list(s)
    n = sl.count('!')
    i = 1

    while i <= n:
        sl.remove('!')
        i += 1
    return ''.join(sl)
