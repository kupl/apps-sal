# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if root is None:
             return 0
         res = []
         self.dfs(root, root.val, res)
         print(res)
         return sum(res)
     
     def dfs(self, root, cur, res):
         if root.left is None and root.right is None:
             res.append(cur)
         if root.left is not None:
             self.dfs(root.left, cur*10+root.left.val, res)
         if root.right is not None:
             self.dfs(root.right, cur*10+root.right.val, res)
