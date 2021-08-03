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
         def helper(n, start):
             if n < 1:
                 return [None]
             
             res = []
             for i in range(1, n+1):
                 lefts = helper(i-1, start)
                 rights = helper(n-i, start+i)
                 
                 for left in lefts:
                     for right in rights:
                         root = TreeNode(i+start)
                         root.left = left
                         root.right = right
                         res.append(root)
                         
             return res
         
         return helper(n, 0) if n else []
             
