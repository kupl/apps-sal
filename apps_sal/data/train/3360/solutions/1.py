def get_chance(n, x, a):
    r = 1
    z = n-x
    while a>0:
        r *= z/n
        n-=1
        z-=1
        a-=1
    return round(r,2)
