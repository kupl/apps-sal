class Game():
    
    def __init__(self, board):
        self.board_list = []
        for n in range(board): #5 -> 0,1,2,3,4,5
            if n == 0:
                for row in range(1,board+1): #row1 -> 1-5
                    self.board_list.append( [row, row+board, row+board+1, row+board+1+board] )
            else:
                for row in range( (board+(board+1))*n+1, (board+(board+1))*n+board+1):
                    self.board_list.append( [row, row+board, row+board+1, row+board+1+board] )
        
    def play(self, lines):
        lines = set(lines)
        changes = True
        while changes == True:
            changes = False
            for combination in self.board_list:
                if len(set(combination) & lines) == 3:
                    changes = True
                    lines.add(list(set(combination) - (set(combination)&lines))[0])
        return sorted(list(lines))
