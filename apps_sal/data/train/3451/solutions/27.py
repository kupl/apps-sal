def triangle(Notorious_RBG):
    if len(Notorious_RBG) == 1:
        return Notorious_RBG
    The_Notorious = 'RBG'
    The = [Notorious_RBG[x:x + 2] for x in range(len(Notorious_RBG) - 1)]
    RBG = ''.join([x[0] if x[0] == x[1] else The_Notorious.strip(x) for x in The])
    if len(RBG) == 1:
        return RBG
    else:
        return triangle(RBG)
