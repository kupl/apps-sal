def isValid(formula):
    mat = [m+1 in formula for m in range(8)]
    return all((
        not (mat[0] and mat[1]),
        not (mat[2] and mat[3]),
        not (mat[4] ^ mat[5]),
        mat[6] or mat[7]
    ))
