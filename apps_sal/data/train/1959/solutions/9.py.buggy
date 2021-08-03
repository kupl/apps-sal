# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         vals = self.in_order_traversal(root)
         min_diff = float('inf')
         for i in range(len(vals) - 1):
             min_diff = min(min_diff, vals[i+1] - vals[i])
         return min_diff
         
     def in_order_traversal(self, root):
         vals = []
         if root is not None:
             vals = self.in_order_traversal(root.left) + [root.val] + self.in_order_traversal(root.right)
         return vals
