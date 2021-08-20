def sum_nested(L):
    if L == []:
        return 0
    if type(L[0]) == int:
        if len(L) == 1:
            return L[0]
        else:
            return L[0] + sum_nested(L[1:])
    else:
        return sum_nested(L[0]) + sum_nested(L[1:])
