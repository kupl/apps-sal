def kontti(w):
    return ' '.join([(lambda pos: ''.join(['ko', s[pos + 1:], '-', s[:pos + 1], 'ntti']))([i for (i, l) in enumerate(s) if l.lower() in 'aeiouy'][0]) if any((l.lower() in 'aeiouy' for l in s)) else s for s in w.split(' ')]) if len(w) else ''
