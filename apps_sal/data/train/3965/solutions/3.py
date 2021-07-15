def powerof4(n):
    t=[int, float]
    if type(n) not in t:
        return False
    if n==1.0:
        return True
    elif n<1.0:
        return False
    return powerof4(n/4.0)
