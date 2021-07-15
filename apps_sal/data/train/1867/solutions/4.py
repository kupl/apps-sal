# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def helper(self,node):
         if node is not None:
             self.helper(node.left)
             self.stack.append(node.val)
             self.helper(node.right)
         
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         self.stack = []
         if root is not None:
             self.helper(root)
             return self.stack[k-1]
         else:
             return None
         
