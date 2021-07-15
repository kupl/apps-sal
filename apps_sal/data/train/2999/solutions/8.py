def hex_word_sum(string):
    string = string.translate(string.maketrans('OS', '05')).split()
    return sum(int(i, 16) for i in string if set(i) <= set('0123456789ABCDEF'))
