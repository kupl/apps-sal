def solve():
    S = [0] + [int(c) for c in input()]
    N = len(S) - 1

    if S[1] == 0:
        return -1
    for n in range(N // 2 + 1):
        if S[n] != S[N - n]:
            return -1
        if S[n] == 1:
            k = n

    E = []
    Q = []
    for n in range(1, k + 1):
        if S[n] == 1:
            for q in Q:
                E.append((q, n))
            Q = []
        Q.append(n)

    E.append((k, k + 1))
    for n in range(k + 2, N + 1):
        E.append((k + 1, n))

    return '\n'.join([" ".join(map(str, e)) for e in E])


print((solve()))
