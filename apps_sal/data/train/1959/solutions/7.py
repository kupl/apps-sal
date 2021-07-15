# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import sys
 class Solution:
     def makeList(self,root):
         if root == None:
             return([])
         else:
             return(self.makeList(root.left) + [root.val] + self.makeList(root.right))
         
     def minDiffInBST(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         arr = self.makeList(root)
         minDistance = sys.maxsize
         
         if len(arr) == 0:
             return(0)
         else:
             for i in range(1,len(arr)):
                 gap = abs(arr[i] - arr[i-1])
                 if gap < minDistance:
                     minDistance = gap
                     
             return(minDistance)
                 
