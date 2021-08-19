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
            if any((r == 'XXX' for r in curState)) or any((r == 'OOO' for r in curState)) or any((''.join([curState[i][j] for i in range(3)]) == 'XXX' for j in range(3))) or any((''.join([curState[i][j] for i in range(3)]) == 'OOO' for j in range(3))) or (curState[0][0] == curState[1][1] == curState[2][2] == 'X') or (curState[0][0] == curState[1][1] == curState[2][2] == 'O') or (curState[0][2] == curState[1][1] == curState[2][0] == 'X') or (curState[0][2] == curState[1][1] == curState[2][0] == 'O'):
                continue
            moves = set()
            for (i, row) in enumerate(curState):
                for (j, cell) in enumerate(row):
                    if cell == ' ' and cell != targetState[i][j]:
                        moves.add((i, j, targetState[i][j]))
            if len(moves) == 0:
                continue
            numX = sum((r.count('X') for r in curState))
            numO = sum((r.count('O') for r in curState))
            if numX == numO:
                curTurn = 'X'
            else:
                curTurn = 'O'
            for (i, j, symbol) in moves:
                if symbol != curTurn:
                    continue
                newState = [curState[t] for t in range(3)]
                newState[i] = curState[i][:j] + curTurn + curState[i][j + 1:]
                stateStack.append(tuple(newState))
        return False
