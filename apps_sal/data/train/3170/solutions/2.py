def longer(s):
    return ' '.join(sorted(s.split(), key=lambda item: (len(item), item)))
