def Dragon(n, strng='Fa'):
    if not isinstance(n, int) or n < 0: return ''
    if not n: return strng.translate(None, "ab")
    next = ''.join("aRbFR" if c == 'a' else "LFaLb" if c == 'b' else c for i,c in enumerate(strng))
    return Dragon(n-1, next)
