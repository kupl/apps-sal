class island:
    """number, x, y"""

    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number


def onelighthouseenough(islands, leftbottom):
    bottomleft = min(islands, key=lambda a: (a.y, a.x))
    if leftbottom == bottomleft:
        print(1)
        print(leftbottom.number, end=' ')
        print(' NE')
        return True
    rightbottom = min(islands, key=lambda a: (-a.x, a.y))
    bottomright = min(islands, key=lambda a: (a.y, -a.x))
    if rightbottom == bottomright:
        print(1)
        print(rightbottom.number, end=' ')
        print(' NW')
        return True
    lefttop = min(islands, key=lambda a: (a.x, -a.y))
    topleft = min(islands, key=lambda a: (-a.y, a.x))
    if lefttop == topleft:
        print(1)
        print(lefttop.number, end=' ')
        print(' SE')
        return True
    righttop = min(islands, key=lambda a: (-a.x, -a.y))
    topright = min(islands, key=lambda a: (-a.y, -a.x))
    if righttop == topright:
        print(1)
        print(righttop.number, end=' ')
        print(' SW')
        return True
    return False


def lighthouses(islands):
    leftbottom = min(islands, key=lambda a: (a.x, a.y))
    if onelighthouseenough(islands, leftbottom):
        return
    islands.remove(leftbottom)
    nextleft = min(islands, key=lambda a: a.x)
    if leftbottom.y < nextleft.y:
        print(2)
        print(leftbottom.number, end=' ')
        print(' NE')
        print(nextleft.number, end=' ')
        print(' SE')
    else:
        print(2)
        print(leftbottom.number, end=' ')
        print(' SE')
        print(nextleft.number, end=' ')
        print(' NE')


T = int(input())
for i in range(T):
    N = int(input())
    islands = []
    for j in range(N):
        (x, y) = list(map(int, input().split()))
        islands.append(island(x, y, j + 1))
    lighthouses(islands)
