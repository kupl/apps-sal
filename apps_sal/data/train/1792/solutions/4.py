"""
def three_by_n_without_hole_missing_top(n):
    # the first column can be _11, _12
    assert n%2 == 1
    if n == 1:
        return 1
    return three_by_n_without_hole_missing_top(n-2) \
        + three_by_n_without_hole(n-1)

def three_by_n_without_hole(n):
    # the first column can be 112, 122, 123
    # the first two cases are the same by symmetry
    assert n%2 == 0
    if n == 0:
        return 1
    return three_by_n_without_hole_missing_top(n-1)*2 \
        + three_by_n_without_hole(n-2)

def three_by_n_with_hole_missing_top(n):
    # the first column can be _X1, _1X, _11, _12
    # the second case is impossible because it would have to look like:
    # _225588...
    # 114477....
    # X336699...
    # the fourth case is divided into two cases,
    # depending on whether the next column is X12 or 312
    assert n%2 == 0
    if n == 0:
        return 0
    return three_by_n_without_hole_missing_top(n-1) \
        + three_by_n_with_hole(n-1) \
        + three_by_n_with_hole_missing_top(n-2) \
        + three_by_n_without_hole(n-2)

def three_by_n_with_hole(n):
    # the first column can be X11, X12, 1X2, 11X, 12X, 112, 122, 123
    # by symmetry:
    # case 4 = case 1
    # case 5 = case 2
    # case 7 = case 6
    # note that case 3 is impossible because it would have to look like:
    # 114477....
    # X225588...
    # 336699....
    assert n%2 == 1
    if n == 1:
        return 2
    return three_by_n_without_hole(n-1)*2            \
        + three_by_n_without_hole_missing_top(n-2)*2 \
        + three_by_n_with_hole_missing_top(n-1)*2    \
        + three_by_n_with_hole(n-2)
"""

# naive algorithm
def mat_mul(A,B):
    n = len(A)
    # the top left entry is A[0][0]*B[0][0] + A[0][1]*B[1][0] + ...
    return [[sum(A[i][k]*B[k][j]%12345787 for k in range(n))%12345787 for j in range(n)] for i in range(n)]

# exponentiation by squaring
def mat_pow(A,k):
    n = len(A)
    res = [[0+(i==j) for j in range(n)] for i in range(n)] # A^0
    while k:
        if k%2 == 1:
            res = mat_mul(res,A)
        A = mat_mul(A,A)
        k //= 2
    return res

# let:
# A = three_by_n_without_hole_missing_top
# B = three_by_n_without_hole
# C = three_by_n_with_hole_missing_top
# D = three_by_n_with_hole
# initial cases:
# A[1] = 1
# B[0] = 1
# C[0] = 0
# D[1] = 2
# recursive formulas:
# A[n] =  A[n-2] +  B[n-1]
# B[n] = 2A[n-1] +  B[n-2]
# C[n] =  A[n-1] +  B[n-2] +  C[n-2] + D[n-1]
# D[n] = 2A[n-2] + 2B[n-1] + 2C[n-1] + D[n-2]
# adjust parity
# A[2k+1] =  A[2(k-1)+1] +  B[2k]
# B[2k]   = 2A[2(k-1)+1] +  B[2(k-1)]
# C[2k]   =  A[2(k-1)+1] +  B[2(k-1)] +  C[2(k-1)] + D[2(k-1)+1]
# D[2k+1] = 2A[2(k-1)+1] + 2B[2k]     + 2C[2k]     + D[2(k-1)+1]
# offset
# A[2k+1] = 3A[2(k-1)+1] +  B[2(k-1)]
# B[2k]   = 2A[2(k-1)+1] +  B[2(k-1)]
# C[2k]   =  A[2(k-1)+1]    B[2(k-1)] +  C[2(k-1)] +  D[2(k-1)+1]
# D[2k+1] = 8A[2(k-1)+1] + 4B[2(k-1)] + 2C[2(k-1)] + 3D[2(k-1)+1]

def three_by_n_without_hole(n):
    res = mat_pow([[3,1],[2,1]],n//2)
    return res[0][0]

def three_by_n_with_hole(n):
    res = mat_pow([[3,1,0,0],[2,1,0,0],[1,1,1,1],[8,4,2,3]],n//2)
    return (res[3][0] + res[3][1] + 2*res[3][3])%12345787

def three_by_n(n):
    if n%2 == 1:
        return three_by_n_with_hole(n)
    return three_by_n_without_hole(n)
