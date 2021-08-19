import collections


class Tower:

    def __init__(self):
        indicesOfAlienPath = []
        shots = 0


class GameStats:

    def __init__(self):
        alienPath = collections.deque()
        towers = []
        waves = collections.deque()


DirEOL = 0
DirLeft = 1
DirRight = 2
DirUp = 3
DirDown = 4


def tower_defense(grid, turrets, aliens):
    game = FromBattlefield(grid, turrets, aliens)
    numSurvivedAliens = 0
    while AnalysisIsRunning(game.alienPath, game.remainingWaves):
        game = PrepareRound(game)
        game.alienPath = KillAliens(game.alienPath, game.towers)
        numSurvivedAliens = numSurvivedAliens + CountAliensLeavingPath(game.alienPath)
    return numSurvivedAliens


def FromBattlefield(grid, turrets, aliens):
    coords = DeterminePathCoordinates(grid)
    game = GameStats()
    game.alienPath = collections.deque([0 for a in range(len(coords))])
    game.towers = CreateTowers(grid, turrets, coords)
    game.remainingWaves = collections.deque(aliens)
    return game


def DeterminePathCoordinates(grid):
    result = []
    coord = GetCoordFor(grid, '0')
    result.append(coord)
    dir = LookForPath(grid, coord, DirEOL)
    while dir != DirEOL:
        coord = GetCoordinate(coord, dir)
        result.append(coord)
        dir = LookForPath(grid, coord, dir)
    return result


def GetCoordFor(grid, id):
    n = len(grid)
    for row in range(n):
        for col in range(n):
            if grid[row][col] == id:
                return (col, row)
    return (0, 0)


def LookForPath(grid, c, dir):
    if IsOnPath(grid, (c[0] + 1, c[1])) and dir != DirLeft:
        return DirRight
    elif IsOnPath(grid, (c[0] - 1, c[1])) and dir != DirRight:
        return DirLeft
    elif IsOnPath(grid, (c[0], c[1] - 1)) and dir != DirDown:
        return DirUp
    elif IsOnPath(grid, (c[0], c[1] + 1)) and dir != DirUp:
        return DirDown
    return DirEOL


def GetCoordinate(orig, dir):
    if dir == DirLeft:
        return (orig[0] - 1, orig[1])
    elif dir == DirRight:
        return (orig[0] + 1, orig[1])
    elif dir == DirUp:
        return (orig[0], orig[1] - 1)
    elif dir == DirDown:
        return (orig[0], orig[1] + 1)
    return orig


def IsOnPath(grid, c):
    n = len(grid)
    return c[1] < n and c[0] < n and (c[1] >= 0) and (c[0] >= 0) and (grid[c[1]][c[0]] == '1' or grid[c[1]][c[0]] == '0')


def CreateTowers(grid, turrets, alienPathCoords):
    towers = []
    for name in sorted(turrets.keys()):
        towerCoords = GetCoordFor(grid, name)
        pathIdxInRange = DetermineIndicesOfAlienPathInRange(alienPathCoords, towerCoords, turrets[name][0])
        towers.append((pathIdxInRange, turrets[name][1]))
    return towers


def DetermineIndicesOfAlienPathInRange(alienPathCoords, towerCoords, dist):
    result = []
    sqrDist = dist * dist
    startY = max(0, towerCoords[1] - dist)
    startX = max(0, towerCoords[0] - dist)
    for y in range(startY, towerCoords[1] + dist + 1):
        for x in range(startX, towerCoords[0] + dist + 1):
            cur = (x, y)
            if cur in alienPathCoords and SqrDistance(cur, towerCoords) <= sqrDist:
                result.append(alienPathCoords.index(cur))
    return sorted(result)


def SqrDistance(left, right):
    y = left[1] - right[1]
    x = left[0] - right[0]
    return x * x + y * y


def AnalysisIsRunning(alienPath, waves):
    return len(waves) > 0 or any(alienPath)


def PrepareRound(game):
    game.alienPath.pop()
    if len(game.remainingWaves) > 0:
        game.alienPath.appendleft(game.remainingWaves.popleft())
    else:
        game.alienPath.appendleft(0)
    return game


def KillAliens(alienPath, towers):
    activeTowers = towers.copy()
    while CanShootAgain(activeTowers):
        (alienPath, activeTowers) = ShootWithTowers(alienPath, activeTowers)
        activeTowers = FilterInactiveTowers(alienPath, activeTowers)
    return alienPath


def CanShootAgain(towers):
    return len(towers) > 0


def ShootWithTowers(alienPath, towers):
    towersShot = []
    for t in towers:
        (alienPath, t) = ShootAliensInFormostPosition(alienPath, t)
        towersShot.append(t)
    return (alienPath, towersShot)


def ShootAliensInFormostPosition(alienPath, tower):
    for idx in reversed(tower[0]):
        if alienPath[idx] > 0:
            shots = tower[1] - 1
            alienPath[idx] = alienPath[idx] - 1
            return (alienPath, (tower[0], shots))
    return (alienPath, tower)


def FilterInactiveTowers(alienPath, towers):
    result = []
    for t in towers:
        if t[1] > 0 and AreAliensInRange(alienPath, t[0]):
            result.append(t)
    return result


def AreAliensInRange(alienPath, towerRange):
    for idx in towerRange:
        if alienPath[idx] > 0:
            return True
    return False


def CountAliensLeavingPath(alienPath):
    return alienPath[-1]
