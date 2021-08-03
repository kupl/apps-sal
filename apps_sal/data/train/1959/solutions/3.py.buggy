# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     prev = float('-inf')
     res = float('inf')
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if root.left:
             self.minDiffInBST(root.left)
         self.res = min(self.res, root.val-self.prev)
         self.prev = root.val
             
         if root.right:
             self.minDiffInBST(root.right)
         
         return self.res
