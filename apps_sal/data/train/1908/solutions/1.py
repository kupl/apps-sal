# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def countNodes1(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if not root:
             return 0
         if root.left is None and root.right is None:
             return 1
         if root.left is None:
             return 1 + self.countNodes(root.right)
         if root.right is None:
             return 1 + self.countNodes(root.left)
         return 1 + self.countNodes(root.right) + self.countNodes(root.left)
 
     def countNodes(self,root):
         p = root 
         height = 0
         while p:
             height += 1
             p = p.left
         if height <= 1:
             return height
         
         p = root
         while p:
             hr = 0
             pr = p.right
             while pr:
                 hr += 1
                 pr = pr.left
             if hr == height - 1:
                 return 2 ** (height-1) + self.countNodes(p.right)
             return 2 ** (height-2) + self.countNodes(p.left)
             
         
         
