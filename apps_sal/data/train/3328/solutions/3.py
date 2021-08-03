def caeser(m, k):
    r = ""
    M = m.upper()
    for c in M:
        if c >= 'A' and c <= 'Z':
            r += chr(65 + (ord(c) - 65 + k) % 26)
        else:
            r += c
    return r
