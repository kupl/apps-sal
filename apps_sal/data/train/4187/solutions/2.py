class Direction:
    North = 0
    East = 1
    South = 2
    West = 3


class Solomon:
    curDir = Direction.North
    xLoc = 0
    yLoc = 0
    timeDepth = 0
    timeFactor = 2


def unpackWayPoint(wayPoint):
    amountTimeDialation = wayPoint[0]
    newDir = wayPoint[1]
    distToTravel = wayPoint[2]
    return (amountTimeDialation, newDir, distToTravel)


def updateHeroDistance(hero, dirOfTravel, trueDistToMove):
    if dirOfTravel == Direction.North:
        hero.yLoc += trueDistToMove
    elif dirOfTravel == Direction.South:
        hero.yLoc -= trueDistToMove
    elif dirOfTravel == Direction.East:
        hero.xLoc += trueDistToMove
    else:
        hero.xLoc -= trueDistToMove


def printDist(hero):
    print(("Hero's location: [", hero.xLoc, ',', hero.yLoc, ']'))


def solomons_quest(wayPoints):
    hero = Solomon()
    for nextStop in wayPoints:
        (amtTimeDialation, dirOfTravel, amtToTravel) = unpackWayPoint(nextStop)
        hero.timeDepth += amtTimeDialation
        trueDistToMove = hero.timeFactor ** hero.timeDepth * amtToTravel
        updateHeroDistance(hero, dirOfTravel, trueDistToMove)
    heroFinalLoc = [hero.xLoc, hero.yLoc]
    return heroFinalLoc
