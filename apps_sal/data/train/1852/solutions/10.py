# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         if not n:
             return []
         return self.generateBST(1,n)
         
     def generateBST(self,start,end):
         res = []
         if start>end:
             res.append(None) 
         for i in range(start,end+1):
             leftlists = self.generateBST(start,i-1)
             rightlists = self.generateBST(i+1,end)
             for left in leftlists:
                 for right in rightlists:
                     root = TreeNode(i)
                     root.left = left
                     root.right = right
                     res.append(root)
         return res 
