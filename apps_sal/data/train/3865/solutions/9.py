def looper(Q, S, R): return [Q + (S - Q) / (R - 1) * V for V in range(R - 1)] + [S]if 1 < R else[Q]
