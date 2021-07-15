def alphabetized(s):
    return ''.join(ch for ch in sorted(s, key=lambda ch: ch.lower()) if ch.isalpha())
