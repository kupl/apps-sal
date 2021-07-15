def isomorph(a, b):
    print((a, b))
    if(len(a) != len(b)):
            return False
    m = {} # mapping of each character in a to b
    r = {} # mapping of each character in b to a
    for i, c in enumerate(a):
        if c in m:
            if b[i] != m[c]:
                return False
        else:
            m[c] = b[i]
        if b[i] in r:
            if c != r[b[i]]:
                return False
        else:
            r[b[i]] = c
    print('True')
    return True
