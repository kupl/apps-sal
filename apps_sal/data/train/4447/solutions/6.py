def revamp(s):
    words = s.split()
    words = [''.join(sorted(w)) for w in words]
    words = sorted(words, key=lambda w: (sum((ord(i) for i in w)), w))
    return ' '.join(words)
