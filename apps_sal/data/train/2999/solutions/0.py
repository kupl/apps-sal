def hex_word_sum(s):
    return sum((int(w, 16) for w in s.translate(str.maketrans('OS', '05')).split() if set(w) <= set('0123456789ABCDEF')))
