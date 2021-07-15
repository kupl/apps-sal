class Solution:
     def judgeCircle(self, moves):
         """
         :type moves: str
         :rtype: bool
         """
         if not moves:
             return True
         if len(moves) % 2 == 1:
             return False
         
         up, left = 0, 0
         for move in moves:
             if move == 'U':
                 up += 1
             if move == 'D':
                 up -= 1
             if move == 'L':
                 left += 1
             if move == 'R':
                 left -= 1
         return up == 0 and left == 0
             

