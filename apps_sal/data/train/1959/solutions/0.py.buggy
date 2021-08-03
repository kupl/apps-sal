# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def addValueToList(self, root, lst):
         if root is not None:
             lst.append(root.val)
             self.addValueToList(root.left, lst)
             self.addValueToList(root.right, lst)
 
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         values = []
         self.addValueToList(root, values)
         sorted_values = sorted(values)
         max_diff = sorted_values[-1] - sorted_values[0]
         for i in range(len(values)-1):
             if sorted_values[i+1] - sorted_values[i] < max_diff:
                 max_diff = sorted_values[i+1] - sorted_values[i]
         return max_diff
