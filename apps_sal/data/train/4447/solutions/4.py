def revamp(s):
  return ' '.join(sorted([''.join(sorted(w)) for w in s.split()], key = lambda w: (sum(ord(c) for c in w), w)))
