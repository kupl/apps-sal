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
         res = []
         def dfs(root, path):
             if not root:
                 return
             if not root.left and not root.right:
                 res.append(path*10+root.val)
                 return
             if root.left:
                 dfs(root.left, path*10 + root.val)
             if root.right:
                 dfs(root.right, path*10 + root.val)
         dfs(root, 0)
         return sum(res)
         
