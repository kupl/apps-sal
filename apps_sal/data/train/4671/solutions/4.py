def isTree(Q):
    if not len(Q):
        return False
    H = [0] * len(Q)
    U = [[-1, 0]]
    while len(U):
        (F, T) = U.pop()
        if H[T]:
            return False
        H[T] = 1
        U += [[T, V] for V in Q[T] if V != F]
    return len(Q) == sum(H)
