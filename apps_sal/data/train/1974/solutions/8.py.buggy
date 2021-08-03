# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         self.post_traversal = []
         if root is None:
             return self.post_traversal
         self.postorderTraversals(root)
         return  self.post_traversal
 
     def postorderTraversals(self, root):
         if root.left:
             self.postorderTraversals(root.left)
         if root.right:
             self.postorderTraversals(root.right)
         self.post_traversal.append(root.val)
         
         
