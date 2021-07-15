# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def traverse(self, root, hold):
         if root.left:
             self.traverse(root.left, hold)
         hold.append(root.val)
         if root.right:
             self.traverse(root.right, hold)
         
     
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         hold = []
         if not root:
             return True
         self.traverse(root, hold)
         size_tree = len(hold)
         for ele in range(size_tree-1):
             if not hold[ele] < hold[ele+1]:
                 return False
         return True
             
