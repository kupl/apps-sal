def feast(beast, dish):
    (fbeast, lbeast) = (beast[0], beast[-1])
    (fdish, ldish) = (dish[0], dish[-1])
    return fbeast == fdish and lbeast == ldish
