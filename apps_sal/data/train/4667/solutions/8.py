def traffic_jam(m, S):
    M = list(m)
    for i in range(len(S))[::-1]:
        R = sum([list(r)for r in zip(M[i:], S[i][::-1])], [])
        M[i:] = R + M[i + len(R) // 2:]
    return ''.join(M)[:M.index('X') + 1]
