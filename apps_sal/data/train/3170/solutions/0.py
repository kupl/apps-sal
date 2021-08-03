def longer(s):
    return ' '.join(sorted(s.split(), key=lambda w: (len(w), w)))
