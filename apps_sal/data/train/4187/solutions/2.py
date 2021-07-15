
#Directions player can move: North is positive y axis, East is positive x axis
class Direction:
    North = 0;  East = 1;  South = 2;  West = 3
#-----end classDirection


#The data of the hero of the story
class Solomon:
    curDir = Direction.North    #default direction is set to facing north
    xLoc = 0            # East and West directions (East is positive x)
    yLoc = 0            # North and South directions (Nortn is positive y)
    timeDepth = 0       #Current depth of the traveler
    timeFactor = 2      #This factor is constant and is based on game definition
#-----end class




def unpackWayPoint(wayPoint):
    amountTimeDialation = wayPoint[0]
    newDir = wayPoint[1]
    distToTravel = wayPoint[2]

    return amountTimeDialation, newDir, distToTravel
#-----end function



def updateHeroDistance(hero, dirOfTravel, trueDistToMove):

    if dirOfTravel == Direction.North:
        hero.yLoc += trueDistToMove
    elif dirOfTravel == Direction.South:
        hero.yLoc -= trueDistToMove
    elif dirOfTravel == Direction.East:
        hero.xLoc += trueDistToMove
    else:
        hero.xLoc -= trueDistToMove

#-----end fucntion

#a small helper debugger function
def printDist(hero):
    print(('''Hero's location: [''', hero.xLoc, ',', hero.yLoc, ']'))


def solomons_quest(wayPoints):
    hero = Solomon()

    for nextStop in wayPoints:
        amtTimeDialation, dirOfTravel, amtToTravel = unpackWayPoint(nextStop)

        #update hero based on the waypoint data
        hero.timeDepth += amtTimeDialation
        trueDistToMove = (hero.timeFactor**hero.timeDepth)*amtToTravel  #dist is based on depth and factor
        updateHeroDistance(hero, dirOfTravel, trueDistToMove)

    #pack data in a list
    heroFinalLoc = [hero.xLoc, hero.yLoc]

    return heroFinalLoc
#-----end function

