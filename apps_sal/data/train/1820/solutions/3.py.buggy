# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def largestValues(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         ret = []
         row = []
         next_row = []
 
         if root:
             next_row.append(root) 
 
         while next_row:
             current_max = None
             row = next_row
             next_row = []
             for node in row:
                 if current_max == None or current_max < node.val:
                     current_max = node.val
                 if node.left:
                     next_row.append(node.left) 
                 if node.right:
                     next_row.append(node.right) 
             ret.append(current_max)
 
         return ret
