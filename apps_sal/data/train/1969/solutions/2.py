# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 def get(root):
     if root is None:
         return []
     s = str(root.val)
     if root.left or root.right:
         return [s + c for c in get(root.left)] + [s + c for c in get(root.right)]
     return [s]
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         return sum(int(c or "0") for c in get(root))
