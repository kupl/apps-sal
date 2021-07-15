# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         return self.preorder(root, sum, [], [])
     
     def preorder(self, root, sum, path, list):
         
         if not root:
             return []
         
         path = path[:]
         path.append(root.val)
     
         if not root.left and not root.right and root.val == sum:
             list.append(path)
             
         if root.left or root.right:
             sum -= root.val
                 
         if root.left:
             list = self.preorder(root.left, sum, path, list)
 
         if root.right:
             list = self.preorder(root.right, sum, path, list)
             
 
         return list
