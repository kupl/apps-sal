def contamination(text, char):
    i, s = 0, ''
    while i < len(text):
        s += char
        i += 1
    return s
