def hamster_me(code, message):
    D, code, lower = {}, set(c for c in code), 'abcdefghijklmnopqrstuvwxyz'

    for c in sorted(code):
        for i, e in enumerate((lower * 2)[lower.index(c):], 1):
            if e in code - {c} or e in D:
                break
            D[e] = c + str(i)

    return ''.join(D[c] for c in message)
