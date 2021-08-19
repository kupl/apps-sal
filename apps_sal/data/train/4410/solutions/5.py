"""
When you're bad at maths....  x)
The complete story in the comments.
"""


def definer(left, nL, right, nR, name):
    (inpL, outL), (inpR, outR) = left[:2], right[:2]
    return (inpL * nL + inpR * nR, outL * nL + outR * nR, left, nL, right, nR, name)


INF = 10**6

"""
TREE DATA:     length as...      left       nL          right       nR          name (debugging)
               inp     out  
"""
C00 = (4, 0, None, None, None, None, "C00")
C2 = (2, 1, None, None, None, None, "C2")
C4 = (4, 1, None, None, None, None, "C4")

C6 = definer(C2, 1, C4, 1, "C6")
C10 = definer(C4, 1, C6, 1, "C10")
C19_6 = definer(C10, 19, C6, 1, "C19_6")
C18_6 = definer(C10, 18, C6, 1, "C18_6")
C19x5_18x1 = definer(C19_6, 5, C18_6, 1, "C19x5_18x1")
C19x4_18x1 = definer(C19_6, 4, C18_6, 1, "C19x4_18x1")
C_x5andx4 = definer(C19x5_18x1, 1, C19x4_18x1, 1, "C_x5andx4")
C_x13andx4 = definer(C_x5andx4, 13, C19x4_18x1, 1, "C_x13andx4")
C_TOP = definer(C_x13andx4, INF, C2, 0, "C_TOP")                # C2 is dummy, here

START = definer(C00, 1, C_TOP, 1, "START")


def count_sixes(n, c=START):

    _, out, left, nL, right, _, name = c

    if left:
        inpL, outL = left[:2]

    if not left:
        return out

    elif n < inpL * nL:
        complete, r = divmod(n, inpL)
        return outL * complete + (left and count_sixes(r, left))

    else:
        return outL * nL + (right and n and count_sixes(n - inpL * nL, right))
