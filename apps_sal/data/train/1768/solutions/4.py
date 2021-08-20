from copy import deepcopy


def insertItem(bag, item, coord):
    bag = deepcopy(bag)
    (height, width) = (len(item), len(item[0]))
    (y, x) = coord
    for i in range(y, y + height):
        for j in range(x, x + width):
            if item[i - y][j - x] != 0:
                bag[i][j] = item[i - y][j - x]
    return bag


def isCorrectVariant(bag, item, coord):
    (height, width) = (len(item), len(item[0]))
    (y, x) = coord
    for i in range(y, y + height):
        for j in range(x, x + width):
            if bag[i][j] and item[i - y][j - x] != 0:
                return False
    return True


def bags_variants(bag, item):
    bags = []
    for i in range(len(bag) - len(item) + 1):
        for j in range(len(bag[0]) - len(item[0]) + 1):
            if isCorrectVariant(bag, item, (i, j)):
                bags.append(insertItem(bag, item, (i, j)))
    return bags


def solve(bag, items):
    if not items:
        return bag
    for temp_bag in bags_variants(bag, items[0]):
        r = solve(temp_bag, items[1:])
        if r:
            return r


def fit_bag(height, width, items):
    bag = [[0] * width for _ in range(height)]
    return solve(bag, items)
