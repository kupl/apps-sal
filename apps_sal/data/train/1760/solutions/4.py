def count(chessBoard):
    caseDict = dict()
    runRow = [[chessBoard[x][y] for y in range(len(chessBoard))] for x in range(len(chessBoard))]
    runCol = [[chessBoard[x][y] for y in range(len(chessBoard))] for x in range(len(chessBoard))]
    runBox = [[chessBoard[x][y] for y in range(len(chessBoard))] for x in range(len(chessBoard))]
    for x in range(0, len(chessBoard)):
        for y in range(0, len(chessBoard)):
            if y != 0:
                runRow[x][y] = runRow[x][y - 1] + 1 if chessBoard[x][y] == 1 else 0
            if x != 0:
                runCol[x][y] = runCol[x - 1][y] + 1 if chessBoard[x][y] == 1 else 0
            if x != 0 and y != 0:
                runBox[x][y] = min(runBox[x - 1][y - 1] + 1, runRow[x][y], runCol[x][y]) if chessBoard[x][y] == 1 else 0
    cnts = [0 for _ in range(len(chessBoard) + 1)]
    for r in runBox:
        for v in r:
            cnts[v] += 1
    for i in range(len(cnts) - 2, -1, -1):
        cnts[i] = cnts[i] + cnts[i + 1]
    for i in range(2, len(cnts)):
        if cnts[i] > 0:
            caseDict[i] = cnts[i]
    return caseDict
