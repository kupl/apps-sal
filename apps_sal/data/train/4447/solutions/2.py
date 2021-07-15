revamp = lambda s: ' '.join(sorted( map(lambda x: ''.join(sorted(x)), s.split()), key = lambda w: (sum(map(ord,w)), len(w), w)  ))
