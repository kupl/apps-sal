(A, S, Z) = (list(range(1000)), set(), [])
while len(Z) < 501:
    for i in A:
        T = set(str(i))
        if not T & S:
            Z += [i]
            S = T
            break
    A.remove(Z[-1])


def find_num(n):
    return Z[n]
