def simple_transposition(text):
    r1 = ''
    r2 = ''
    for ch in range(len(text)):
        if ch % 2 == 0:
            r1 += text[ch]
        if ch % 2 == 1:
            r2 += text[ch]
    transpo = r1 + r2
    return transpo
