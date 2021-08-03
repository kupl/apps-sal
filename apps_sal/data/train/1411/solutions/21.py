from math import pi, ceil

T = int(input())
for t in range(T):
    X, R, A, B = map(int, input().split())
    turn = 2 * pi * R
    D = turn * X
    time = D / max(A, B)
    d = time * min(A, B)
    delta = D - d
    print(ceil(delta / turn) - 1)
