def capitalize(s):
    return [''.join((ch.upper() if i % 2 == 0 else ch for (i, ch) in enumerate(s))), ''.join((ch.upper() if i % 2 == 1 else ch for (i, ch) in enumerate(s)))]
