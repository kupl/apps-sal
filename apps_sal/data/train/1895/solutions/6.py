class Solution:
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         targetState = tuple(board)
         
         startingState = ('   ', '   ', '   ')
         
         stateStack = [startingState]
         visited = set()
         
         while len(stateStack) > 0:
             curState = stateStack.pop()
             
             if curState == targetState:
                 return True
                 
             if curState in visited:
                 continue
                 
             visited.add(curState)
             
             # Has a player won, thus ending the game?
             if any(r == 'XXX' for r in curState) or any(r == 'OOO' for r in curState) \
                or any(''.join([curState[i][j] for i in range(3)]) == 'XXX' for j in range(3)) or any(''.join([curState[i][j] for i in range(3)]) == 'OOO' for j in range(3)) \
                or (curState[0][0] == curState[1][1] == curState[2][2] == 'X') \
                or (curState[0][0] == curState[1][1] == curState[2][2] == 'O') \
                or (curState[0][2] == curState[1][1] == curState[2][0] == 'X') \
                or (curState[0][2] == curState[1][1] == curState[2][0] == 'O'):
                continue
             
             # What moves are there that get closer to the target state?
             moves = set()
             for i,row in enumerate(curState):
                 for j,cell in enumerate(row):
                     if cell == ' ' and cell != targetState[i][j]:
                         moves.add((i,j,targetState[i][j]))
                         
             # Can only add X's and O's
             if len(moves) == 0:
                 continue
                 
             # Now detect *valid* moves; whose turn is it? 
             numX = sum(r.count('X') for r in curState)
             numO = sum(r.count('O') for r in curState)
             
             if numX == numO:
                 curTurn = 'X'
             else:
                 curTurn = 'O'
                 
             # Make each valid move
             for i,j,symbol in moves:
                 if symbol != curTurn:
                     continue
                 # Valid move; spawn a new board state
                 newState = [curState[t] for t in range(3)]
                 newState[i] = curState[i][:j] + curTurn + curState[i][j+1:]
                 stateStack.append(tuple(newState))
                 
         return False
