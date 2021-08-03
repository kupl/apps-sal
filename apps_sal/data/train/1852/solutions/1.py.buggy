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
         if n <= 0:
             return []
         
         mem = {}
         
         return self.genTrees(mem, 1, n)
     
     def genTrees(self, mem, start, end):
         cached = mem.get((start, end))
         if cached != None:
             return cached
         
         if start > end:
             return [None]
         
         if start == end:
             return [TreeNode(start)]
         
         retVal = []
         for i in range(start, end + 1):
             left = self.genTrees(mem, start, i - 1)
             right = self.genTrees(mem, i + 1, end)
             
             for lnode in left:
                 for rnode in right:
                     root = TreeNode(i)
                     root.left = lnode
                     root.right = rnode
                     retVal.append(root)
 
         mem[(start, end)] = retVal
         return retVal

