import itertools


def reg_sum_hits(diceAmount, sides):

    possibilities = calculatepermutations(sides, diceAmount)

    sumvalues = calculatesumvalues(sides, diceAmount)

    distributionofsums = calculatedist(possibilities, sumvalues)

    return distributionofsums


def calculatepermutations(sides, diceAmount):
    facevalues = (i for i in range(1, sides + 1))
    allpermutations = itertools.product(facevalues, repeat=diceAmount)
    return [sum(i) for i in allpermutations]


def calculatesumvalues(sides, diceAmount):
    biggestnumber = sides * diceAmount
    smallestnumber = diceAmount
    return (i for i in range(smallestnumber, biggestnumber + 1))


def calculatedist(possibilities, sumvalues):
    return [[i, possibilities.count(i)] for i in sumvalues]
