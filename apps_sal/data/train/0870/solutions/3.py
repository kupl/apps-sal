t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    (o, z, oz, zo, ozo, zoz) = (0, 0, 0, n, n, n)
    for i in s:
        if i == '1':
            zo = min(zo, z)
            z = z + 1
            ozo = min(ozo, oz)
            oz = oz + 1
            zoz = zoz + 1
        else:
            oz = min(oz, o)
            o = o + 1
            zoz = min(zoz, zo)
            zo = zo + 1
            ozo = ozo + 1
    print(min(o, z, oz, zo, ozo, zoz))
