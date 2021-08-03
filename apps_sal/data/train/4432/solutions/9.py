def can_jump(A):
    z = len(A)
    for i in range(z - 1)[::-1]:
        z = (z, i)[z <= i + A[i]]
    return z == 0
