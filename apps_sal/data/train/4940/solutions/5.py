def shut_the_gate(s):
    return '|'.join((w.translate({ord(c): set(w) & set('RH'[i:] or '@') and '.' or c for (i, c) in enumerate('VARCH')}) for w in '@'.join(3 * [s]).split('|'))).split('@')[1]
