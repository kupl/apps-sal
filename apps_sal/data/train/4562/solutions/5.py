def snap(F, T, S=None, P=True):
    if not T:
        return 0
    if S is None:
        S = []
    S.append(F.pop(0) if P else T.pop(0))
    if len(S) > 1 and S[-1] == S[-2]:
        F.extend(S)
        return 1 + snap(F, T)
    return snap(F, T, S, not P)
