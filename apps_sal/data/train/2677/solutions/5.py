D = {v:(r, c) for r, row in enumerate(['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/', 'U ??????']) for c, v in enumerate(row)}

mind = lambda d, mx: min(d, mx - d)
move = lambda t, lastr, lastc, r, c: (t + mind(abs(r - lastr), 6) + mind(abs(c - lastc), 8) + 1, r, c)

def tv_remote(words):

    t, lastr, lastc, lower = 0, 0, 0, True
    
    for e in words:
        if e.isalpha() and lower != e.islower():
            t, lastr, lastc = move(t, lastr, lastc, 5, 0)
            lower = not lower
        t, lastr, lastc = move(t, lastr, lastc, *D[e.lower()])
    return t    
