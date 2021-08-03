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
         if not root:
             return []
         
         l = [root]
         r = False
         ret = []
         
         while l:
             values = [node.val for node in l]
             if r:
                 values.reverse()
             ret.append(values)
             tmp = []
             for node in l:
                 if node.left:
                     tmp.append(node.left)
                 if node.right:
                     tmp.append(node.right)
             l = tmp
             r = not r
             
         return ret
