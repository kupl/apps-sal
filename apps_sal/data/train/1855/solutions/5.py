# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def isValidBST(self, node):
         """
         :type root: TreeNode
         :rtype: bool
         """
         def valid(somenode, ceiling, floor):
             if somenode is None:
                 return True
             if somenode.val >= ceiling or somenode.val <= floor:
                 return False
             
             
             return valid(somenode.left, somenode.val, floor) and valid(somenode.right, ceiling, somenode.val)
         
         return valid(node, sys.maxsize, -sys.maxsize)
             
             
          
         
