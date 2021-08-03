# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         # Time: O(|V| + |E|) = O(n)
         # Space: O(log(n))
         def isValid(node, lo, hi):
             if lo != None:
                 if node.val <= lo:
                     return False
             if hi != None:
                 if node.val >= hi:
                     return False
             if node.left != None:
                 if not isValid(node.left, lo, node.val):
                     return False
             if node.right != None:
                 if not isValid(node.right, node.val, hi):
                     return False
             return True
         
         if root == None: return True
         return isValid(root, None, None)
