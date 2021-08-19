def spinning_rings(inner_max, outer_max):
    p = inner_max + 1
    q = outer_max + 1
    move = 1
    while -move % p != move % q:
        if -move % p >= q:
            move = move // p * p + p - q + 1
        elif move % q >= p:
            move = move // q * q + q
        elif -move % p > move % q and (-move % p + move % q) % 2 == 0:
            move += (-move % p - move % q) // 2
        else:
            move = min((move - 1) // p * p + p, (move - 1) // q * q + q) + 1
    return move
