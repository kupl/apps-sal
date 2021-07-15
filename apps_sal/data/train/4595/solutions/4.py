def bishop_diagonal(A, B):
    t = lambda x: (ord(x[0]) - 97, 8 - int(x[1]))
    I = lambda x: ''.join([chr(97 + x[0]), str(8 - x[1])])
    a1, a2 = t(A)
    b1, b2 = t(B)
    if a1 + a2 != b1 + b2 and a1 - a2 != b1- b2:
        return sorted([B, A])
    E =((a1-b1)//abs(a1-b1), (a2-b2)//abs(a2-b2))
    while min(a1, a2) != 0 and max(a1, a2) != 7:
        a1 += E[0]
        a2 += E[1]
    while min(b1, b2) != 0 and max(b1, b2) != 7:
        b1 -= E[0]
        b2 -= E[1]
    return sorted([I((a1,a2)), I((b1, b2))])
