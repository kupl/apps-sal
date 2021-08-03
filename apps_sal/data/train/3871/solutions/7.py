def binary_simulation(Q, S):
    Q, L, R = int(Q, 2), len(Q), []
    for S in S:
        if S[0] < 'L':
            Q ^= (1 << L - S[1] + 1) - 1
            Q ^= (1 << L - S[2]) - 1
        else:
            R.append('1' if Q & (1 << L - S[1]) else '0')
    return R
