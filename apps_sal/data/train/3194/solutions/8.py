def berserk_rater(synopsis):
    s = 0
    for sentence in synopsis:
        if 'clang' in sentence.lower():
            s += 5
        elif 'cg' in sentence.lower():
            s -= 2
        else:
            s -= 1
    if s < 0:
        return 'worstest episode ever'
    elif s > 10:
        return 'bestest episode ever'
    else:
        return str(s)
