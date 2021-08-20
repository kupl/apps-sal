def traffic_jam(estrada, rua_lateral):
    X = estrada.index('X')
    principal = list(estrada[:X + 1])
    for i in reversed(range(min(X, len(rua_lateral)))):
        tmp = []
        for j in range(1, min(len(principal) - i - 1, len(rua_lateral[i])) + 1):
            tmp.append(rua_lateral[i][-j])
            tmp.append(principal[i + j])
        principal[i + 1:i + len(tmp) // 2 + 1] = tmp
    return ''.join(principal)
