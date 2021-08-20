import re


def H(Q):
    (M, R) = ({F: re.findall('P(\\d+)', V) for (F, V) in re.findall('p(\\d+)([^q]+)', Q)}, [9000000000.0, 0])

    def H(V, S=set(), C=0):
        if V in S:
            R[:] = (min(R[0], C), max(R[1], C))
            return 9
        S.add(V)
        T = 0
        for B in M[V]:
            T = H(B, S, -~C) or T
        R[0] = R[0] if T else 0
        S.remove(V)
        return R[0]
    for V in re.findall('P(\\d+)', re.sub('p(\\d+)([^q]+)', '', Q)):
        H(V)
    return [R[0] if R[0] < 9000000000.0 else 0, R[1]]


magiCallDepthNumber = magic_call_depth_number = H
