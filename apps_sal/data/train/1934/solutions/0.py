# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if root is None:
             return []
         
         res = []
         level_num = 1
         level = [root]
         
 
         while len(level) != 0:
             level_size = len(level)
             level_res = [None]*level_size
             for i in range(level_size):
                 curr = level.pop(0)
                 level_res[i] = curr.val
                 if curr.left is not None:
                     level.append(curr.left)
                 if curr.right is not None:
                     level.append(curr.right)
             if level_num % 2:
                 res.append(level_res)
             else:
                 level_res.reverse()
                 res.append(level_res)
             level_num += 1
             
         return res
         
         
         
         
