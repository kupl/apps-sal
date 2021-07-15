solve=lambda Q,S:1 if any(V in Q[1+F:] and V not in S for F,V in enumerate(Q)) else 2
