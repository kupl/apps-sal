def alternateCase(s):
    final = []
    for l in s:
        if l == l.lower():
            final.append(l.upper())
        elif l == l.upper():
            final.append(l.lower())
        else:
            final.append(' ')

    return ''.join(final)
