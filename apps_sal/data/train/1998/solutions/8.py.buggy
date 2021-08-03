from functools import reduce
 from collections import deque
 class Solution:
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         hashtable, queue, steps = {}, deque(), None
         startstr = ''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]])
         options = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]] # possible locations to switch for each position of 0
         queue.append([startstr, 0]) # [string to check, current num of steps]
         
         # function to switch characters in a string
         def move(string, moveto, currenti):
             moving = string[moveto]
             string = string.replace(moving, 'x',)
             string = string.replace('0', moving)
             return string.replace('x', '0')
         
         # loop through and add to queue until solution is found or all variations are examined
         while (len(queue) > 0 and steps == None):
             curr = queue.popleft()
             if curr[0] == "123450":
                 steps = curr[1]
                 break
             if curr[0] not in hashtable:
                 currenti = curr[0].find('0')
                 hashtable[curr[0]] = True
                 possibilities = [move(curr[0], i, currenti) for i in options[currenti]]
                 for el in possibilities:
                     queue.append([el, curr[1] + 1])
 
         return -1 if steps == None else steps
