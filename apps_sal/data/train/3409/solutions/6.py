
class Fish:
    size = 1
    intake = 0


def attemptDigestion(myFish, menuItem):
    if menuItem <= myFish.size:
        myFish.intake += menuItem


def assessGrowth(myFish):
    if myFish.intake >= 4 * myFish.size:
        myFish.intake = myFish.intake - 4 * myFish.size
        myFish.size += 1


def fish(str):
    foodPool = []
    foodPool[:0] = str
    foodPool.sort()

    myFish = Fish()

    while foodPool and int(foodPool[0]) <= myFish.size:
        menuItem = int(foodPool.pop(0))
        attemptDigestion(myFish, menuItem)
        assessGrowth(myFish)

    return myFish.size
