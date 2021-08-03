def binary_simulation(s, q):

    outlst = []
    for op in q:
        ini = op[1] - 1

        if op[0] == 'Q':
            outlst.append(s[ini])
        elif op[0] == 'I':
            transl = s[ini:op[2]].maketrans('01', '10')
            s = s[:ini] + s[ini:op[2]].translate(transl) + s[op[2]:]
    return outlst
