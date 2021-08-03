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
         if root is None:
             return True
         self.output_list = []
         self.recurse(root)
         print(self.output_list)
         for i in range(len(self.output_list) - 1):
             if self.output_list[i+1] <= self.output_list[i]:
                 return False
         return True
         
     def recurse(self, root):
         """
         :type root: TreeNode
         """
 
         if root.left is not None and root.right is not None:
             self.recurse(root.left)
             self.output_list.append(root.val)
             self.recurse(root.right)
         elif root.left is not None:
             self.recurse(root.left)
             self.output_list.append(root.val)
         elif root.right is not None:
             self.output_list.append(root.val)
             self.recurse(root.right)
         else:
             self.output_list.append(root.val)
         
