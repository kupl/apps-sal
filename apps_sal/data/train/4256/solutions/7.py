def insert_missing_letters(s):
    (found, inside) = (set(), set(s.upper()))
    return ''.join((a if a in found else found.add(a) or a + ''.join((c for c in map(chr, range(ord(a) - 31, 91)) if c not in inside)) for a in s))
