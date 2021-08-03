# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     
     diff = float('inf')
     prev = float('inf')
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.traversal(root)
         return self.diff
     
     def traversal(self, node):
         
         if node == None:
             return
         
         self.traversal(node.left)
         
         self.diff = min(self.diff, abs(node.val - self.prev))
         self.prev = node.val
          
         
         self.traversal(node.right)
         
     
         
         return
         
