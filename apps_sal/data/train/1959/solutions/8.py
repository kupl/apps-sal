# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from math import inf
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if not root:
             return 0
         
         self.ans = inf
         self.dfs(-inf, root, inf)
         return self.ans
     
     def dfs(self, left, root, right):
         self.ans = min(root.val - left, self.ans, right - root.val)
         if root.left:
             self.dfs(left, root.left, root.val)
         
         if root.right:
             self.dfs(root.val, root.right, right)
