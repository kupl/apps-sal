def crap(garden, bags, cap):
    s = ''.join([''.join(i) for i in garden])
    return 'Dog!!' if 'D' in s else 'Clean' if s.count('@') <= bags * cap else 'Cr@p'
