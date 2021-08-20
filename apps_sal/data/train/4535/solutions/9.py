def zfunc(string):
    if not string:
        return []
    strlen = len(string)
    Z = [0] * strlen
    L = R = 0
    for i in range(1, strlen):
        if i > R:
            L = R = i
            while R < strlen and string[R - L] == string[R]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < strlen and string[R - L] == string[R]:
                    R += 1
                Z[i] = R - L
                R -= 1
    Z[0] = strlen
    return Z
