# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         if not root:
             return 0
         
         distanceToLeft = self.dfs(root.left)
         if distanceToLeft + 1 == k:
             return root.val
         elif distanceToLeft + 1< k:
             return self.kthSmallest(root.right, k - distanceToLeft - 1)
         else:
             return self.kthSmallest(root.left, k)
     
     def dfs(self, root):
         if not root:
             return 0
         left = self.dfs(root.left)
         right = self.dfs(root.right)
         return left + right + 1
