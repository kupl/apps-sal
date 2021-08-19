def play_if_enough(Q, S):
    R = {}
    for T in Q:
        R[T] = 1 + R[T] if T in R else 1
    for T in S:
        if T not in R or R[T] < 1:
            return (False, Q)
        R[T] -= 1
    return (True, ''.join((V * R[V] for (F, V) in enumerate(R))))
