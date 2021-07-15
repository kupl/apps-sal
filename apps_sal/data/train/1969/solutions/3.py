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
         # using dfs
         #   when leafnode (add the dfs number to the final sum)
         return self.dfs(root, 0)
         
     def dfs(self, node, num):
         if not node:
             return 0
         newNum = num * 10 + node.val
         if not node.right and not node.left:
             return newNum
         return self.dfs(node.right, newNum) + self.dfs(node.left, newNum)
