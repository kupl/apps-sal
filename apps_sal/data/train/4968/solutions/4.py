G=lambda Q,S : G(S,Q % S) if S else Q
relatively_prime = lambda Q,S : [S for S in S if 1 == G(Q,S)]
