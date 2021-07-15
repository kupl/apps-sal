import numpy as np

board = np.array(list('abcde123fghij456klmno789pqrst.@0uvwxyz_/')).reshape(5,8)
board = {v:i for i,v in np.ndenumerate(board)}

def tv_remote(word):
    '''I'm not happy with this messy stuff'''
    x,y = (0,0)
    result = 0
    for letter in word:
        x1,y1 = board[letter]
        result += abs(x-x1) + abs(y-y1) + 1
        x,y = x1,y1
    return result
