def chameleon(chameleons, desiredColor):
    color = chameleons.pop(desiredColor)
    d,r = divmod(abs(chameleons[0]-chameleons[1]),3)
    if d < color and r == 0:
        return min(chameleons) + 3 * d
    else:
        return -1
