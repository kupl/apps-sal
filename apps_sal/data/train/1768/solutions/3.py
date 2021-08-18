def ItemFitsInBag(bag, item, y0, x0):
    for y in range(y0, y0 + len(item)):
        for x in range(x0, x0 + len(item[0])):
            if bag[y][x] != 0 and item[y - y0][x - x0] != 0:
                return False
    return True


def removeItem(bag, item, y0, x0):
    ID = max([max(i) for i in item])
    for y in range(y0, y0 + len(item)):
        for x in range(x0, x0 + len(item[0])):
            if bag[y][x] == ID:
                bag[y][x] = 0
    return bag


def FitItemInBag(bag, item, y0, x0):
    for y in range(y0, y0 + len(item)):
        for x in range(x0, x0 + len(item[0])):
            if item[y - y0][x - x0] != 0:
                bag[y][x] = item[y - y0][x - x0]
    return bag


def PossibleCoords(bag, item, height, width):
    p = []
    itemHeight = len(item)
    itemWidth = len(item[0])
    for y in range(height - itemHeight + 1):
        for x in range(width - itemWidth + 1):
            if ItemFitsInBag(bag, item, y, x):
                p.append([y, x])
    return p


def Loop(bag, height, width, items, itemINDEX):

    if itemINDEX == len(items):
        return bag

    item = items[itemINDEX]

    possibilities = PossibleCoords(bag, item, height, width)

    for p in possibilities:
        y = p[0]
        x = p[1]

        bag = FitItemInBag(bag, item, y, x)

        bag = Loop(bag, height, width, items, itemINDEX + 1)

        for i in bag:
            if max([max(i) for i in items[-1]]) in i:
                return bag

        bag = removeItem(bag, item, y, x)

    return bag


def fit_bag(height, width, items):

    bag = [[0] * width for i in range(height)]

    itemINDEX = 0

    bag = Loop(bag, height, width, items, itemINDEX)

    return bag
