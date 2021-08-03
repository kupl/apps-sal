# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if root is None:
             return []
         q = [(root, 0)]
         res = []
         prev_lvl = -1
         while q:
             current, lvl = q[0]
             q.pop(0)
             if lvl > prev_lvl:
                 res.append([current.val])
             else:
                 res[-1].append(current.val)
             prev_lvl = lvl
             if current.left:
                 q.append((current.left, lvl + 1))
             if current.right:
                 q.append((current.right, lvl + 1))
         return res
         
         
         
