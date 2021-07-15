# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 import sys
 
 class Solution:
     def isValidBST(self, root):
         return isBSTUtil(root, -sys.maxsize, sys.maxsize)
     
 
 def isBSTUtil(root, min, max):
     if root == None:
         return True
     
     if root.val <= min or root.val >= max:
         return False
     
     return isBSTUtil(root.left, min, root.val) and isBSTUtil(root.right, root.val, max)
