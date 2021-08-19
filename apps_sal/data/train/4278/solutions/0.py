def diagonal(m):
    P = sum((m[i][i] for i in range(len(m))))
    S = sum((m[i][-i - 1] for i in range(len(m))))
    if P > S:
        return 'Principal Diagonal win!'
    elif S > P:
        return 'Secondary Diagonal win!'
    else:
        return 'Draw!'
