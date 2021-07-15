class SubrectangleQueries(object):

    def __init__(self, rectangle):
        self.rectangle = copy.deepcopy(rectangle)

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue
        return self.rectangle

    def getValue(self, row, col):
        return self.rectangle[row][col]
