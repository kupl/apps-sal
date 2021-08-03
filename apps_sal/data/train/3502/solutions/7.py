def solution(x=None, *args):
    args = args + (x,)
    tam1 = len(args)
    tam2 = len(set(args))
    if tam1 == 0:
        return False
    if tam1 == 1:
        if 1 in args:
            return True
        else:
            return False
    elif tam1 != tam2:
        return True
    else:
        return False
