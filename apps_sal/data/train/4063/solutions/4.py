def evenator(s):
    return ' '.join((e + e[-1] if len(e) % 2 else e for e in [''.join((c for c in w if c.isalnum())) for w in s.split()] if e != ''))
