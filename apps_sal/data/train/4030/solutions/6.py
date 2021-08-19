def radix_tree(*Q):
    (U, R) = (set(Q), {})
    for Q in Q:
        T = R
        for Q in Q:
            if not Q in T:
                T[Q] = {}
            T = T[Q]

    def H(Q, S):
        T = list(Q)
        for V in T:
            if 1 == len(Q[V]) and S + V not in U:
                B = next(iter(Q[V]))
                Q[V + B] = Q[V][B]
                del Q[V]
                T.append(V + B)
            else:
                H(Q[V], S + V)
    H(R, '')
    return R
