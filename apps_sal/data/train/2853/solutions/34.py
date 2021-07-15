def solve(A,Z=[]):
    for x in A[::-1]:Z=[x]*(x not in Z)+Z
    return Z
