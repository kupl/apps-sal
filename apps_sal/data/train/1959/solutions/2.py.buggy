# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.min = float('inf')
         self.prev = None
         self.dfs(root)
         return self.min
     
     def dfs(self, node):
         if not node:
             return
         self.dfs(node.left)
         if self.prev:
             self.min = min(self.min, node.val - self.prev.val)
         self.prev = node
         self.dfs(node.right)
         
