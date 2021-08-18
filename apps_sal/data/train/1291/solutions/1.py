
dirTable = {}
dirTable["R"] = (1, 0)
dirTable["L"] = (-1, 0)
dirTable["D"] = (0, -1)
dirTable["U"] = (0, 1)


def readCoordinates():
    strX, strY, strDir = input().split()
    x = int(strX)
    y = int(strY)
    dx, dy = dirTable[strDir]
    return x, y, dx, dy


t = int(input())
for test in range(t):
    xe, ye, dxe, dye = readCoordinates()
    n = int(input())
    shortest = 1000
    for i in range(n):
        xa, ya, dxa, dya = readCoordinates()
        xa -= xe
        ya -= ye
        dxa -= dxe
        dya -= dye

        if dxa == 0 and dya == 0:
            continue
        elif dxa == 0:
            if xa != 0:
                continue
            else:
                time = -ya * 1.0 / dya
                if 0 < time < shortest:
                    shortest = time
        elif dya == 0:
            if ya != 0:
                continue
            else:
                time = -xa * 1.0 / dxa
                if time > 0 and time < shortest:
                    shortest = time
        else:
            tx = -xa * 1.0 / dxa
            ty = -ya * 1.0 / dya
            if tx == ty and 0 < tx < shortest:
                shortest = tx
    if shortest < 1000:
        print("%.1f" % shortest)
    else:
        print("SAFE")
