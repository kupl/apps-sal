# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 def dfs(lst, root):
     if root != None:
         lst.append(root.val)
         dfs(lst, root.left)
         dfs(lst, root.right)
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         lst = []
         dfs(lst, root)
         lst.sort()
         res = float('inf')
         for i in range(1, len(lst)):
             res = min(res, lst[i] - lst[i - 1])
         return res
         
