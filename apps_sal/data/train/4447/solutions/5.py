def revamp(s):
    s = [''.join(sorted(i)) for i in s.split()]
    return ' '.join(sorted(s, key=lambda x: (sum((ord(i) for i in x)), len(x), x)))
