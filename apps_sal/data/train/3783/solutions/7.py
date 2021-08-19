def frame(text, c):
    mx = max((len(w) for w in text))
    return '\n'.join([c * (mx + 4)] + [c + ' ' + w.ljust(mx) + ' ' + c for w in text] + [c * (mx + 4)])
