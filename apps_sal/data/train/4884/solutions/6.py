def connect_the_dots(paper):
    laliste = paper[:-1].split('\n')
    tablo = [[' ' for i in range(len(laliste[0]))] for j in range(len(laliste))]
    lesPositions = []
    for (i, ligne) in enumerate(laliste):
        listeCar = list(ligne)
        for (j, car) in enumerate(listeCar):
            if 97 <= ord(car) <= 122:
                lesPositions.append((car, i, j))
    lesPositions.sort(key=lambda x: x[0])
    pointA = lesPositions.pop()
    while lesPositions:
        pointB = lesPositions.pop()
        if pointA[1] == pointB[1]:
            ext = [pointB[2], pointA[2]]
            for y in range(min(ext), max(ext) + 1):
                tablo[pointA[1]][y] = '*'
        elif pointA[2] == pointB[2]:
            ext = [pointB[1], pointA[1]]
            for x in range(min(ext), max(ext) + 1):
                tablo[x][pointA[2]] = '*'
        else:
            dx = 1 if pointA[1] < pointB[1] else -1
            dy = 1 if pointA[2] < pointB[2] else -1
            y = pointA[2]
            for x in range(pointA[1], pointB[1] + dx, dx):
                tablo[x][y] = '*'
                y += dy
        pointA = pointB
    tablo2 = [''.join(ligne) + '\n' for ligne in tablo]
    return ''.join(tablo2)
