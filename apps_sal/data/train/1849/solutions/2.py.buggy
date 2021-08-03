# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def traverse(self, root, ordered, level=0):
         if root.left:
             self.traverse(root.left, ordered, level=level+1)
         for create in range(level-len(ordered)+1):
             ordered.append([])
         ordered[level].append(root.val)
         if root.right:
             self.traverse(root.right, ordered, level=level+1)
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if not root:
             return []
         ordered = [[]]
         self.traverse(root, ordered, level=0)
         return ordered
