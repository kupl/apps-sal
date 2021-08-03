def clonewars(kata):
    return [2**(kata - 1), sum(2**i * (kata - i) for i in range(kata))] if kata else [1, 0]
