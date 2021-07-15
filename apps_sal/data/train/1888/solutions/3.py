# Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def addOneRow(self, root, v, d):
         """
         :type root: TreeNode
         :type v: int
         :type d: int
         :rtype: TreeNode
         """
         if d == 1:
             rt = TreeNode(v)
             rt.left = root
             return rt
         
         def DFS(rt, depth):
             if depth == d - 1:
                 newL = TreeNode(v)
                 newL.left = rt.left
                 newR = TreeNode(v)
                 newR.right = rt.right
                 rt.left = newL
                 rt.right = newR
                 return
             if rt.left:
                 DFS(rt.left, depth + 1)
             if rt.right:
                 DFS(rt.right, depth + 1)
         
         DFS(root, 1)
         return root
             
                 
     
             
