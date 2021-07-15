
#All data associated to the fish 
class Fish:
    size = 1        #Determines what the fish can eat
    intake = 0      #determines when fish grows in size
#---end class Fish


def attemptDigestion(myFish, menuItem):
    if menuItem <= myFish.size:    #Scenario: Eat the current menue item
        myFish.intake += menuItem
#---end function attemptDigestion

#Based on rules of the game, we grow (in size by 1) when what we have intaked is larger than or equal to the 
# size of our fish.  The cost to increase in size is equal to four times the current size of our fish
# e.g. intake ==14, size is 3.  The req to size 4 is 12 units, so our size increases by 1 and our
# intake is reduced as: 14 - 4*3 = 2 (intake is now 2; we burnt 12 units to inc in size :)
def assessGrowth(myFish):
    if myFish.intake >= 4*myFish.size:  #Situation: the fish is ready to grow in size 1
        myFish.intake =  myFish.intake - 4*myFish.size  #deplete the amount it cost us to inc. in size 
        myFish.size+=1
#---end fuction assessGrowth

def fish(str):
    #Convert the string of fish-sizes to a list
    foodPool = [] 
    foodPool[:0] = str
    foodPool.sort()     #ascending order

    myFish = Fish()

    #Begin the eating and evolving game
    while foodPool and int(foodPool[0]) <= myFish.size:
        menuItem = int(foodPool.pop(0))
        attemptDigestion(myFish, menuItem)  
        #determine if we need to level up based on mySize and the intake
        assessGrowth(myFish)

    #----end while

    return myFish.size

#---end function fishGame

