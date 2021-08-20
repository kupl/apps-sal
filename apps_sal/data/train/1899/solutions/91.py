class Solution:

    def __init__(self):
        self.islandA = []
        self.islandB = []
        self.maxRow = 0
        self.maxColumn = 0
        self.maps = []
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.maps = A
        self.maxRow = len(A) - 1
        self.maxColumn = len(A[0]) - 1
        for row in range(len(A)):
            for column in range(len(A[row])):
                value = A[row][column]
                if value == 1:
                    if len(self.islandA) == 0:
                        self.islandA = self.floodFill(A, self.islandA, row, column)
        stack = self.islandA
        print(stack)
        steps = 0
        while stack:
            temp = []
            for st in stack:
                for direction in self.directions:
                    nextColumn = st[0] + direction[0]
                    nextRow = st[1] + direction[1]
                    if nextColumn < 0 or nextColumn > self.maxColumn or nextRow < 0 or (nextRow > self.maxRow) or (A[nextColumn][nextRow] == 2):
                        continue
                    if A[nextColumn][nextRow] == 1:
                        return steps
                    A[nextColumn][nextRow] = 2
                    temp.append([nextColumn, nextRow])
            steps += 1
            stack = temp
        return 1

    def floodFill(self, A, island, row, column):
        if [row, column] not in island:
            island.append([row, column])
            A[row][column] = 2
        for direction in self.directions:
            nextColumn = column - direction[0]
            nextRow = row - direction[1]
            if nextColumn < 0 or nextColumn > self.maxColumn or nextRow < 0 or (nextRow > self.maxRow):
                continue
            if self.maps[nextRow][nextColumn] == 1 and [nextRow, nextColumn] not in island:
                island = self.floodFill(A, island, nextRow, nextColumn)
        return island
