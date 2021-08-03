def spidey_swings(Q):
    End = At = Pos = 0
    Left = []
    for V in Q:
        Left.append(End)
        End += V[1]
    Left.append(End)
    R = []
    while At < len(Q):
        L = I = 0
        F = At
        while F < len(Q):
            W = Q[F][0] - 20
            T = int((W * W - (W - 30) ** 2) ** .5)
            if Left[F] <= Pos + T:
                if End < Pos + T + T:
                    T = max(1 + End - Pos >> 1, Left[F] - Pos)
                if Left[1 + F] < Pos + T:
                    T = Left[1 + F] - Pos
                U = End <= Pos + T + T
                W = (T * T + (Q[F][0] - 50) ** 2) ** .5
                W = (T + T if Pos + T + T < End else End - Pos) / W
                if L < W or not I and U:
                    N, L = T, W
                I = U
            F += 1
        R.append(Pos + N)
        Pos += N + N
        while At < len(Left) and Left[At] <= Pos:
            At += 1
        At -= 1
    return R
