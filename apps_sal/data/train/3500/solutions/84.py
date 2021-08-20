def remove_exclamation_marks(s):
    d = ''
    for i in s:
        if i not in '!¡':
            d += i
    return d
