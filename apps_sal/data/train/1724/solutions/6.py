class alien:
    def __init__(self, speed, i, j):
        self.speed=speed
        self.positionI=i
        self.positionJ=j

class model:

    def __del__(self):
        print(' ')

    def __init__ (self, aliens, defender):
        self.listOfAllAliens=[]
        self.listOfShootableAliens=[]
        self.countOfStaticAliens=0
        self.blastSequence=[]
        self.roundOfGame=0
        self.gameWon=False
        self.gameOver=False
        self.TESTnumberOfAliens=0

        self.positionOfDefenderI=defender[1]
        self.positionOfDefenderJ=defender[0]

        self.lenOfFieldJ=defender[0]
        self.lenOfFieldI=len(aliens[0])

        self.createAliens(aliens)

        self.countStaticAliens()

    def createAliens(self, aliens):
        posJ=-1

        for line in aliens:
            posJ = posJ + 1
            for i in range (0, len(aliens[0])):
                newAlien = alien (line[i], i, posJ)
                self.TESTnumberOfAliens = self.TESTnumberOfAliens + 1
                self.listOfAllAliens.append(newAlien)

    def countStaticAliens(self):
        for alien in self.listOfAllAliens:
            if (alien.speed == 0):
                self.countOfStaticAliens = self.countOfStaticAliens+1

    def increaseRoundOfGame (self):
        self.roundOfGame = self.roundOfGame + 1


    def moveAliens (self):

        for alien in self.listOfAllAliens:
            self.calculateAlienMovement(alien)

            if (alien.positionJ == self.positionOfDefenderJ):
                self.gameOver=True
            
            if (alien.positionI == self.positionOfDefenderI):
                # for whatever reason, static aliens are not shot
                if(alien.speed != 0):
                    self.putAlienInListOfShootableAliens(alien)
        

    
    def calculateAlienMovement(self, alien):
        speed=alien.speed
        distance = speed+alien.positionI



        TESTdistance = abs(speed)
        distance_remaining = 0

        TESTpositionI = alien.positionI
        TESTpositionJ = alien.positionJ

        # only horizontal movement
        if (distance <= self.lenOfFieldI-1 and distance >= 0):
            alien.positionI = distance
            TESTdistance = 0
        
        # vertical movement right
        elif(distance >= self.lenOfFieldI):
            # move to rightmost column
            distance_right = self.lenOfFieldI -1 - alien.positionI
            distance_remaining = abs(alien.speed) - distance_right
            alien.positionI = alien.positionI + distance_right 

            TESTdistance = TESTdistance - distance_right
            
            # move up
            alien.positionJ = alien.positionJ+1
            distance_remaining = distance_remaining - 1

            TESTdistance = TESTdistance - 1
            
            alien.speed = -alien.speed

            # move left
            alien.positionI = alien.positionI -distance_remaining

            TESTdistance = TESTdistance - distance_remaining
            
        
        # vertical movement left
        elif(distance < 0):

            # move to leftmost column
            distance_left = alien.positionI
            distance_remaining = abs(alien.speed) - distance_left
            alien.positionI = 0

            TESTdistance = TESTdistance - distance_left

            # move up
            alien.positionJ = alien.positionJ+1
            distance_remaining = distance_remaining - 1

            TESTdistance = TESTdistance - 1
            
            alien.speed = -alien.speed

            # move right
            alien.positionI = distance_remaining

            TESTdistance = TESTdistance - distance_remaining
        

        else:
            if(speed !=0):
                print('error! alien movement could not be calculated')

        if (
            (TESTpositionI == alien.positionI) 
        and (TESTpositionJ == alien.positionJ)
        and (alien.speed!=0)
        ):
            print('error! alien did not move this round')

        if(TESTdistance != 0):
            print('error! calculation went wrong. remaining or negative distance left.')

        

    def putAlienInListOfShootableAliens (self, shootableAlien):
        self.listOfShootableAliens.append(shootableAlien)



    def shoot(self):

        if not (len(self.listOfShootableAliens)==0):
            # there will be a shot!
            alienToBeShot = self.findAlienToBeShot()
            
            self.deleteShotAlienFromListOfAllAliens(alienToBeShot)

            self.addRoundToBlastSequence()

        # in any case:
        self.clearListOfShootableAliens()


    def clearListOfShootableAliens(self):
        self.listOfShootableAliens=[]

    def findAlienToBeShot(self):
        iterator = self.lenOfFieldJ-1
        alienFound = False
        killingList=[]

        while ((iterator >= 0) and (alienFound == False)):
            # iterate through the field by lines
            for shootableAlien in self.listOfShootableAliens:
                if ((shootableAlien.positionJ == iterator) and (shootableAlien.positionI == self.positionOfDefenderI)):
                    killingList.append(shootableAlien)
                    alienFound = True
            iterator = iterator -1

        # TEST
        if(len(killingList)==0):
            print(("error! no alien to be shot found, also there are some!"
            + "in the listofshootable Aliens", self.listOfShootableAliens))
            return None
        
        elif (len(killingList)==1):
            return killingList[0]
        
        else:
            return self.findAlienWithHighestAbsoluteSpeed(killingList)


    def findAlienWithHighestAbsoluteSpeed(self, killingList):
        maxAbsSpeed=0
        highestAlien=[]

        # calculate highest speed
        for alien in killingList:
            if ( abs(alien.speed) > maxAbsSpeed):
                maxAbsSpeed = abs(alien.speed)

        # find fastest alien
        for alien in killingList:
            if ( abs(alien.speed) == maxAbsSpeed):
                highestAlien.append(alien)
        
        #more than one fastest aliens 
        if (len(highestAlien)>1):
            # choose a right-moving alien
            for alien in highestAlien:
                if (alien.speed > 0):
                    return alien

        # return any of the remaining aliens
        return highestAlien[0]
        

    def addRoundToBlastSequence (self):
        self.blastSequence.append(self.roundOfGame)

    def deleteShotAlienFromListOfAllAliens(self, shotAlien):
  
        if (shotAlien.speed == 0):
            self.countOfStaticAliens = self.countOfStaticAliens-1
            print(('error! static alien shot in round',self.roundOfGame ))

        self.listOfAllAliens.remove(shotAlien)



    def checkIfGameOverOrGameWon (self):

        if ((len(self.listOfAllAliens)-self.countOfStaticAliens) == 0):
            self.gameWon = True

        if ((self.gameOver == True) or (self.gameWon == True)):
            return True

        else:
            return False



# Section of Testing

    def TESTNumberOfAliens (self):

        if (self.TESTnumberOfAliens != (len(self.listOfAllAliens) + len(self.blastSequence))):
            print("error! Something went wrong. the number of aliens is not matching" )
            
        if(self.TESTnumberOfAliens < len(self.blastSequence)):
            print('error! more aliens shot than existed')



def blast_sequence(aliens,position):
    
    game = model(aliens, position)
    check = False

    while (not check):
        game.TESTNumberOfAliens()
        game.moveAliens()
        game.shoot()
        check = game.checkIfGameOverOrGameWon()
        game.increaseRoundOfGame()
    
    isGameWon = game.gameWon
    solution = game.blastSequence
    del game
    if (isGameWon):
        return solution
    else:
        return None



