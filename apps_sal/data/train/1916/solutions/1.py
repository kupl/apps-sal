# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import sys
 
 class Solution:
     def __init__(self):
         self.max = -sys.maxsize
         
     def maxPathSum(self, root):
         self.mps(root)
         return self.max
     
     def mps(self, root):
         # returns max path-to-leaf from ROOT
         if not root.left and not root.right: 
             self.max = max(self.max, root.val)
             return root.val
         if not root.left and root.right:
             right = self.mps(root.right)
             self.max = max(self.max, root.val, root.val + right)
             return max(root.val, root.val + right)
         if root.left and not root.right: 
             left = self.mps(root.left)
             self.max = max(self.max, root.val, root.val + left)
             return max(root.val, root.val + left)
         left = self.mps(root.left)
         right = self.mps(root.right)
         self.max = max(self.max, root.val, left + root.val, root.val + right, left + root.val + right)
         return max(root.val, left + root.val, right + root.val)

