def validSolution(board):
    for x in range(9):
        arr = [board[y][x] for y in range(9)]
        arr2 = [board[x][y] for y in range(9)]
        arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
        for i in range(9):
            if arr[i] in arr[(i+1):]: return False
            if arr2[i] in arr2[(i+1):]: return False
            if arr3[i] in arr3[(i+1):]: return False
    return True
