from functools import reduce
 from collections import deque
 class Solution:
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         hashtable = {}
         end, steps = "123450", None
         startstr = ''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]])
         options = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
         queue = deque()
         queue.append([startstr, 0])
         
         def move(currstr, moveto, currenti):
             moving = currstr[moveto]
             currstr = currstr.replace(moving, '!',)
             currstr = currstr.replace('0', moving)
             currstr = currstr.replace('!', '0')
             return currstr
         
         while (len(queue) > 0 and steps == None):
             currstr = queue.popleft()
             if currstr[0] == end:
                 steps = currstr[1]
                 break
 
             if currstr[0] not in hashtable:
                 currenti = currstr[0].find('0')
                 hashtable[currstr[0]] = True
                 possibilities = [move(currstr[0], i, currenti) for i in options[currenti]]
                 for el in possibilities:
                     queue.append([el, currstr[1] + 1])
 
         return -1 if steps == None else steps
