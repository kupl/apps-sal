def add_point(ori, dis, c):
    lastPoint = c[-1]
    if ori == 'N':
        c.append((lastPoint[0], lastPoint[1] + dis))
    elif ori == 'S':
        c.append((lastPoint[0], lastPoint[1] - dis))
    elif ori == 'E':
        c.append((lastPoint[0] + dis, lastPoint[1]))
    else:
        c.append((lastPoint[0] - dis, lastPoint[1]))


def check_corner(l_o):
    ini = l_o[0]
    fin = l_o[-1]
    if ini == fin:
        return False
    if ini == 'N' or ini == 'S':
        ini = 'V'
    else:
        ini = 'H'
    if fin == 'N' or fin == 'S':
        fin = 'V'
    else:
        fin = 'H'
    if ini == fin:
        return False
    return True


def check_intersect(rectas):
    u = rectas[-1]
    ux = [u[0][0], u[1][0]]
    ux.sort()
    uy = [u[0][1], u[1][1]]
    uy.sort()
    oriU = ''
    if ux[0] == ux[1]:
        oriU = 'V'
    if uy[0] == uy[1]:
        oriU = 'H'
    for r in rectas[:-2]:
        rx = [r[0][0], r[1][0]]
        rx.sort()
        ry = [r[0][1], r[1][1]]
        ry.sort()
        oriR = ''
        if rx[0] == rx[1]:
            oriR = 'V'
        if ry[0] == ry[1]:
            oriR = 'H'
        if oriU == oriR:
            if oriU == 'V' and ux[0] == rx[0]:
                if ry[0] <= uy[0] <= ry[1] or ry[0] <= uy[1] <= ry[1]:
                    return True
                if uy[0] < ry[0] and uy[1] > ry[1]:
                    return True
            if oriU == 'H' and uy[0] == ry[0]:
                if rx[0] <= ux[0] <= rx[1] or rx[0] <= ux[1] <= rx[1]:
                    return True
                if ux[0] < rx[0] and ux[1] > rx[1]:
                    return True
        elif oriU == 'V':
            if uy[0] <= ry[0] <= uy[1]:
                if rx[0] < ux[0] and rx[1] > ux[0]:
                    return True
        elif oriU == 'H':
            if ux[0] <= rx[0] <= ux[1]:
                if ry[0] < uy[0] and ry[1] > uy[0]:
                    return True
        else:
            return False


def calc_area(camino):
    parN = camino[-1][0] * camino[0][1] - camino[-1][1] * camino[0][0]
    for p in range(1, len(camino)):
        par = camino[p - 1][0] * camino[p][1] - camino[p - 1][1] * camino[p][0]
        parN += par
    return abs(parN) / 2


def mouse_path(s):
    camino = [(0, 0)]
    distancia = 0
    listaOrientaciones = ['E']
    rectas = []
    for c in s:
        orientacion = listaOrientaciones[-1]
        if c.isdigit():
            distancia = distancia * 10 + int(c)
        else:
            add_point(orientacion, distancia, camino)
            rectas.append((camino[-2], camino[-1]))
            if check_intersect(rectas):
                return None
            if c == 'L':
                if orientacion == 'N':
                    listaOrientaciones.append('O')
                elif orientacion == 'S':
                    listaOrientaciones.append('E')
                elif orientacion == 'E':
                    listaOrientaciones.append('N')
                else:
                    listaOrientaciones.append('S')
            elif orientacion == 'N':
                listaOrientaciones.append('E')
            elif orientacion == 'S':
                listaOrientaciones.append('O')
            elif orientacion == 'E':
                listaOrientaciones.append('S')
            else:
                listaOrientaciones.append('N')
            distancia = 0
    add_point(orientacion, distancia, camino)
    rectas.append((camino[-2], camino[-1]))
    if check_intersect(rectas):
        return None
    if camino[-1] != (0, 0):
        return None
    if not check_corner(listaOrientaciones):
        return None
    return calc_area(camino)
