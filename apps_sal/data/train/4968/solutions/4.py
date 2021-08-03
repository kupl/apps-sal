def G(Q, S): return G(S, Q % S) if S else Q
def relatively_prime(Q, S): return [S for S in S if 1 == G(Q, S)]
