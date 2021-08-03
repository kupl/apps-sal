def W(Q, S):
    Q = float(Q)
    B = Q < 0
    Q = abs(Q)
    return '%03d*%02d\'%06.3f"%s' % (Q, Q % 1 * 60, 3600 * Q % 60, S[B])


def convert_to_dms(Q, S): return (W(Q, 'NS'), W(S, 'EW'))
