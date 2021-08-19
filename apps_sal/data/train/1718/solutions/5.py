from copy import deepcopy
import queue


class MazeSymbols(object):
    START_TILE = 'k'
    WALL_TILE = '#'
    WALKABLE_TILE = ' '


class MazeStatus(object):
    FOUND_EXIT = 1
    NO_EXIT_EXISTS = 2
    CONTINUE_SEARCH = 3
    MAZE_VALID = 4
    MAZE_ERROR_NO_START = 5
    MAZE_ERROR_DUPLICATE_START = 6


class MazeSolver(object):

    def __init__(self, mazeBoard):
        self.mazeBoard = deepcopy(mazeBoard)
        self.numRows = len(self.mazeBoard)
        self.numCols = len(self.mazeBoard[0])
        (validStatus, startRow, startCol) = self.__validateMaze__(self.mazeBoard)
        if validStatus == MazeStatus.MAZE_VALID:
            self.validMaze = True
        else:
            self.validMaze = False
        self.startRow = startRow
        self.startCol = startCol

    def isValidMaze(self):
        return self.validMaze

    def attemptSolve(self):
        nR = self.numRows
        nC = self.numCols
        hasVisited = [[False for _ in range(nC)] for _ in range(nR)]
        mazeWalkResult = self.__walkMaze__(self.mazeBoard, hasVisited, nR, nC, self.startRow, self.startCol)
        return mazeWalkResult

    def __validateMaze__(self, mazeBoard):
        startPos = self.__findStartPosition__(mazeBoard)
        if not startPos:
            return (MazeStatus.MAZE_ERROR_NO_START, -1, -1)
        elif len(startPos) >= 2:
            return (MazeStatus.MAZE_ERROR_DUPLICATE_START, -1, -1)
        else:
            startRow = startPos[0][0]
            startCol = startPos[0][1]
            return (MazeStatus.MAZE_VALID, startRow, startCol)

    def __findStartPosition__(self, mazeBoard):
        startPos = []
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.mazeBoard[i][j] == MazeSymbols.START_TILE:
                    startPos.append([i, j])
        return startPos

    def __inImage__(self, i, j, nR, nC):
        if 0 <= i and i < nR and (0 <= j) and (j < nC):
            return True
        else:
            return False

    def __isDesiredCell__(self, img, hasVisited, i, j):
        if img[i][j] == MazeSymbols.WALKABLE_TILE and (not hasVisited[i][j]):
            return True
        else:
            return False

    def __markCellAsVisited__(self, hasVisited, i, j):
        hasVisited[i][j] = True

    def __foundExit__(self, curR, curC, nR, nC):
        upStep = curR - 1
        downStep = curR + 1
        leftStep = curC - 1
        rightStep = curC + 1
        if not self.__inImage__(upStep, curC, nR, nC):
            return True
        elif not self.__inImage__(downStep, curC, nR, nC):
            return True
        elif not self.__inImage__(curR, leftStep, nR, nC):
            return True
        elif not self.__inImage__(curR, rightStep, nR, nC):
            return True
        else:
            return False

    def __foundDuplicateStartPos__(self, img, curR, curC):
        if img[curR][curC] == MazeSymbols.START_TILE:
            return True
        else:
            return False

    def __checkMazeStatus__(self, img, curR, curC, nR, nC):
        if self.__foundExit__(curR, curC, nR, nC):
            return MazeStatus.FOUND_EXIT
        elif self.__foundDuplicateStartPos__(img, curR, curC):
            return MazeStatus.MAZE_ERROR_DUPLICATE_START
        else:
            return MazeStatus.CONTINUE_SEARCH

    def __walkMaze__(self, img, hasVisited, nR, nC, iRoot, jRoot):
        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        numSearchDirs = len(di)
        (iConnected, jConnected) = ([], [])
        q = queue.Queue()
        q.put((iRoot, jRoot))
        self.__markCellAsVisited__(hasVisited, iRoot, jRoot)
        if self.__foundExit__(iRoot, jRoot, nR, nC):
            return MazeStatus.FOUND_EXIT
        while q.empty() == False:
            (u, v) = q.get()
            iConnected.append(u)
            jConnected.append(v)
            for s in range(numSearchDirs):
                iNew = u + di[s]
                jNew = v + dj[s]
                if self.__inImage__(iNew, jNew, nR, nC) and self.__isDesiredCell__(img, hasVisited, iNew, jNew):
                    self.__markCellAsVisited__(hasVisited, iNew, jNew)
                    q.put((iNew, jNew))
                    currentStatus = self.__checkMazeStatus__(img, iNew, jNew, nR, nC)
                    if currentStatus != MazeStatus.CONTINUE_SEARCH:
                        return currentStatus
        return MazeStatus.NO_EXIT_EXISTS


def has_exit(maze):
    m = MazeSolver(maze)
    if not m.isValidMaze():
        raise ValueError('Maze Not Valid')
    else:
        resultSolve = m.attemptSolve()
        if resultSolve == MazeStatus.FOUND_EXIT:
            return True
        elif resultSolve == MazeStatus.NO_EXIT_EXISTS:
            return False
