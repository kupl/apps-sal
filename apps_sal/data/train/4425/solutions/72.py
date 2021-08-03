def mango(q, p):
    Q = q / 3 * 2
    Q = int(Q) if Q % 1 == 0 else int(Q) + 1
    return Q * p
