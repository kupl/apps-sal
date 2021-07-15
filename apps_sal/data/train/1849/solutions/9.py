# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         res = []
         if not root:
             return res
         
         stack = [root]
         row = [root.val]
         
         while stack:
             res += [row]
             tempstack = []
             temprow = []
             
             for n in stack:
                 if n.left:
                     tempstack += [n.left]
                     temprow += [n.left.val]
                 if n.right:
                     tempstack += [n.right]
                     temprow += [n.right.val]
             row = temprow
             stack = tempstack
         return res
                     
                 
             
