def trace(matrix):
    matrixLen = len(matrix)
    if matrixLen == 0:
        return None
    matrixElemsLens = [len(i) for i in matrix]
    for i in matrixElemsLens:
        if i != matrixLen:
            return None
    totalTrace = 0
    currentElem = 0
    for row in matrix:
        totalTrace += row[currentElem]
        currentElem += 1
    return totalTrace
