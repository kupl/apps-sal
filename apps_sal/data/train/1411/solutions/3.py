import numpy as np
T = int(input())
for i in range(T):
    S = input().split(' ')
    X = int(S[0])
    R = int(S[1])
    A = int(S[2])
    B = int(S[3])
    d = int(abs(A - B) * X / max(A, B))
    if X * abs(A - B) % max(A, B) == 0:
        d = d - 1
    print(d)
