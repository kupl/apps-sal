S1 = 1
 S2 = 2
 S3 = 3
 S4 = 4
 S5 = 5
 
 class Solution(object):
 
     def __init__(self):
         self.state = S1
 
     def removeComments(self, source):
         """
         :type source: List[str]
         :rtype: List[str]
         """
         ret = []
         buf = []
         for s in source:
             for c in s:
                 if self.state in [S1, S2]:
                     buf.append(c)
                 elif self.state == S4:
                     if len(buf) >= 2 and buf[len(buf) - 2: len(buf)] == ['/','*']:
                         buf.pop()
                         buf.pop()
                 elif self.state == S3:
                     if len(buf) >= 2 and buf[len(buf) - 2: len(buf)] == ['/', '/']:
                         buf.pop()
                         buf.pop()
                 self._transite(c)
             self._transite('\n')
             if len(buf) != 0 and self.state in [S1, S2]:
                 ret.append(''.join(buf))
                 buf = []
         return ret
 
 
     def _transite(self, char):
         if self.state == S1:
             if char == '/':
                 self.state = S2
             else:
                 self.state = S1
         elif self.state == S2:
             if char == '/':
                 self.state = S3
             elif char == '*':
                 self.state = S4
             else:
                 self.state = S1
 
         elif self.state == S3:
             if char == '\n':
                 self.state = S1
             else:
                 self.state = S3
 
         elif self.state == S4:
             if char == '*':
                 self.state = S5
             else:
                 self.state = S4
 
         elif self.state == S5:
             if char == '/':
                 self.state = S1
             elif char == '*':
                 self.state = S5
             else:
                 self.state = S4
         return self.state
