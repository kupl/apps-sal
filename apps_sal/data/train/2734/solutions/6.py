import math


def distance(pos1, pos2):
    if pos1 and pos2:
        return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)


def peaceful_yard(yard, min_distance):
    rPos = None
    lPos = None
    mPos = None
    counter = 0
    for i in range(len(yard)):
        if yard[i].find("L") != -1:
            lPos = (i, yard[i].find("L"))
            counter += 1
        if yard[i].find("R") != -1:
            rPos = (i, yard[i].find("R"))
            counter += 1
        if yard[i].find("M") != -1:
            mPos = (i, yard[i].find("M"))
            counter += 1
    if counter <= 1:
        return True
    else:
        distances = [distance(rPos, lPos), distance(lPos, mPos), distance(rPos, mPos)]
        for dist in distances:
            if (dist and dist < min_distance):
                return False
        return True
