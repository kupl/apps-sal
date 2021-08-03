def points(Q): return sum(3 * (V[0] > V[2]) + (V[0] == V[2])for V in Q)
