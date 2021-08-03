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
         if(root == None):
             return []
         rowmax = []
         self.findRowMax(root, 1, rowmax)
         return rowmax
         
         
     def findRowMax(self, root, level, rowmax):
         if(level > len(rowmax)):
             rowmax.append(root.val)
         else:
             if(root.val > rowmax[level-1]):
                 rowmax[level-1] = root.val
         if(root.left != None):
             self.findRowMax(root.left, level+1, rowmax)
         if(root.right != None):
             self.findRowMax(root.right, level+1, rowmax)
