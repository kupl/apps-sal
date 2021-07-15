# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     sol = []
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         self.sol = []
         if root is None:
             return True 
         self.traverseBST(root)
         print(self.sol)
         for i in range(1,len(self.sol)):
             if self.sol[i] <= self.sol[i-1]:
                 return False
         return True
     
     # def isValid(self,root):
     #     if root.left and root.right:
     #         if root.left.val< root.val and root.right.val>root.val:
     #             return True
     #     elif root.left:
     #         if root.left.val< root.val:
     #             return True
     #     elif root.right:
     #         if root.right.val>root.val:
     #             return True
     #     else:
     #         return True
     #     return False
 
     
     def traverseBST(self, root):
         if root.left:
             self.traverseBST(root.left)
         print(root.val)
         self.sol.append(root.val)
         # if not self.isValid(root):
         #     return False
         if root.right:
             self.traverseBST(root.right)
         return True
         
