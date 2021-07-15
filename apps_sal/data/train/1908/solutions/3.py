# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def countNodes(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if not root:
             return 0
         h = height(root)
         res = 0
         while root:
             if height(root.right) == h-1:
                 res += 1<<h
                 root = root.right
             else:
                 res += 1<<(h-1)
                 root = root.left
             h -= 1
             
         return res
 
 def height(node):
     if not node:
         return -1
     else:
         return 1+height(node.left)
