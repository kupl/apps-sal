# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from copy import deepcopy
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if not root:
             return []
         left2rightq = [root]
         right2leftq = []
         result = []
         while left2rightq or right2leftq:
             if left2rightq:
                 line = []
                 while left2rightq:
                     tmp = left2rightq.pop(-1)
                     line.append(tmp.val)
                     if tmp.left:
                         right2leftq.append(tmp.left)
                     if tmp.right:
                         right2leftq.append(tmp.right)
                     else:
                         pass
                 result.append(line)
             else:
                 line = []
                 while right2leftq:
                     tmp = right2leftq.pop()
                     line.append(tmp.val)
                     if tmp.right:
                         left2rightq.append(tmp.right)
                     if tmp.left:
                         left2rightq.append(tmp.left)
 
                     else:
                         pass
                 result.append(line)
         return result
                 
         
