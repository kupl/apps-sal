def insert_missing_letters(s):
    s, lst, found, inside = s.lower(), [], set(), set(s.upper())
    for a in s:
        lst.append(a if a in found else
                   a + ''.join(c for c in map(chr, range(ord(a)-31,91)) if c not in inside) )
        found.add(a)
        
    return ''.join(lst)
