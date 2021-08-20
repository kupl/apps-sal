def evenize_word(w):
    return w + w[-1] if len(w) % 2 else w


def evenator(s):
    s = ''.join((c for c in s if c.isspace() or c.isalnum()))
    return ' '.join((evenize_word(w) for w in s.split()))
