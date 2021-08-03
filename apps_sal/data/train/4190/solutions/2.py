def is_alt(s):
    a = s[::2]
    b = s[1::2]
    if (b[0] in 'aeiou'):
        c = a
        a = b
        b = c
    return all(x in 'aeiou' for x in a) and all(x not in 'aeiou' for x in b)
