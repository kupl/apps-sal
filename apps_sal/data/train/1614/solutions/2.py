def who_is_winner(pieces_position_list):

    grid = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]   
            
    columns = 7
    rows = 6
    rowPosition = 0
    winner = None
    drawCount = 0
    
    for piece in pieces_position_list:
        if piece[2] == "Y":
            code = 2
        else:
            code = 1
            
        if piece[0] == "A":
            columnPosition = 0
        elif piece[0] == "B":
            columnPosition = 1
        elif piece[0] == "C":
            columnPosition = 2
        elif piece[0] == "D":
            columnPosition = 3
        elif piece[0] == "E":
            columnPosition = 4
        elif piece[0] == "F":
            columnPosition = 5
        elif piece[0] == "G":
            columnPosition = 6
            
        while grid[rowPosition][columnPosition] != 0:
            if grid[5][columnPosition] == 1 or grid[5][columnPosition] == 2:
                break
            rowPosition += 1       
        grid[rowPosition][columnPosition] = code
        rowPosition = 0
        
        #check horizontal positions for winner
        for row in range(rows):
            for column in range(columns-3):
                if grid[row][column] == 1 and grid[row][column+1] == 1 and grid[row][column+2] == 1 and grid[row][column+3] == 1:
                    winner = "Red"
                elif grid[row][column] == 2 and grid[row][column+1] == 2 and grid[row][column+2] == 2 and grid[row][column+3] == 2:
                    winner = "Yellow"
                    
        #check vertical positions
        for row in range(rows-3):
            for column in range(columns):
                if grid[row][column] == 1 and grid[row+1][column] == 1 and grid[row+2][column] == 1 and grid[row+3][column] == 1:
                    winner = "Red"
                elif grid[row][column] == 2 and grid[row+1][column] == 2 and grid[row+2][column] == 2 and grid[row+3][column] == 2:
                    winner = "Yellow"
                    
        #check left vertical positions
        for row in range(3,rows):
            for column in range(columns-3):
                if grid[row][column] == 1 and grid[row-1][column+1] == 1 and grid[row-2][column+2] == 1 and grid[row-3][column+3] == 1:
                    winner = "Red"
                elif grid[row][column] == 2 and grid[row-1][column+1] == 2 and grid[row-2][column+2] == 2 and grid[row-3][column+3] == 2:
                    winner = "Yellow"
        
        #check right vertical positions
        for row in range(rows-3):
            for column in range(columns-3):
                if grid[row][column] == 1 and grid[row+1][column+1] == 1 and grid[row+2][column+2] == 1 and grid[row+3][column+3] == 1:
                    winner = "Red"
                elif grid[row][column] == 2 and grid[row+1][column+1] == 2 and grid[row+2][column+2] == 2 and grid[row+3][column+3] == 2:
                    winner = "Yellow"

        #check winning condition
        if winner == "Red":
            return "Red"
            break
        elif winner == "Yellow":
            return "Yellow"
            break
            
    if winner == None:
        return "Draw"
    
        
        

