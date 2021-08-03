from collections import deque
 
 class Solution:
     def largestValues(self, root):
         if root is None: return []
         q = deque([(root, 0)])
         l = [root.val]
         # l contains the largest values in each level from 0 to len(l) - 1
         while len(q) != 0:
             (node, level) = q.pop()
             if level == len(l) - 1:
                 l[-1] = max(l[-1], node.val)
             else:
                 l.append(node.val)
             if node.left:
                 q.appendleft((node.left, level + 1))
             if node.right:
                 q.appendleft((node.right, level + 1))
         
         return l
