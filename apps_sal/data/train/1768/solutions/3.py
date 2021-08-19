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

    # If the final item has been placed in the bag then end the loop
    if itemINDEX == len(items):
        return bag

    # Choose item
    item = items[itemINDEX]

    # Coordinate possibilities of item in bag
    possibilities = PossibleCoords(bag, item, height, width)

    # Try the possible locations to place the item in the bag
    for p in possibilities:
        y = p[0]
        x = p[1]

        # Fit the item in the bag
        bag = FitItemInBag(bag, item, y, x)

        # Trigger backtracking
        bag = Loop(bag, height, width, items, itemINDEX + 1)

        # If the final item has been places then end the loop
        for i in bag:
            if max([max(i) for i in items[-1]]) in i:
                return bag

        # Remove the item  so that it can be differently placed
        bag = removeItem(bag, item, y, x)

    return bag


def fit_bag(height, width, items):

    # Initialize bag with zeros
    bag = [[0] * width for i in range(height)]

    # Initialize item index
    itemINDEX = 0

    # Begin the loop
    bag = Loop(bag, height, width, items, itemINDEX)

    return bag
