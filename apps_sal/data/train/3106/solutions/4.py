M = {}


def H(Q, S):
    if Q < S:
        return 0
    if S < 2:
        return 0 < S
    if (Q, S) not in M:
        M[Q, S] = S * H(Q - 1, S) + H(Q - 1, S - 1)
    return M[Q, S]


def combs_non_empty_boxes(Q, S):
    return 'It cannot be possible!' if Q < S else H(Q, S)
