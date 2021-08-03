# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     
     def inOrderTravel(self,root):
         res = []
         if root == None:
             return []
         
         res += self.inOrderTravel(root.left)
         res.append(root.val)
         res += self.inOrderTravel(root.right)
         
         return res
     
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         res  = self.inOrderTravel(root)
         for i in range(1, len(res)):
             if res[i] <= res[i-1]:
                 return False
         
         return True
         
         
         
         
