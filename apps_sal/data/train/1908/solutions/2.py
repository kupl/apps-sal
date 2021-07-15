# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findHeight(self, node):
         return -1 if node is None else 1 + self.findHeight(node.left)
         
     def countNodes(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         h = self.findHeight(root)
         return 0 if h == -1 else ((1 << h) + self.countNodes(root.right) 
                                   if self.findHeight(root.right) == h-1 else (1 << h-1) + self.countNodes(root.left))
