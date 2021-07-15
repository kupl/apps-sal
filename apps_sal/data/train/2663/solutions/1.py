from itertools import product

def addsup(a1, a2, a3):
    goal = set(a3).__contains__
    return [[x, y, x+y] for x,y in product(a1, a2) if goal(x+y)]
