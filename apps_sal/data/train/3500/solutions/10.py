def remove_exclamation_marks(s):
    y = list(s)
    for l in range(0, y.count('!')):
        y.remove('!')
    z = ''.join(y)
    return z
