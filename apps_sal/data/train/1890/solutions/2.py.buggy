# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findBottomLeftValue(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         
         leftmost = []
         
         def recurse(node, path):
             nonlocal leftmost
             
             if node is None:
                 return
             
             if len(path) > len(leftmost):
                 leftmost = path
                 
             if 0 < len(path) == len(leftmost):
                 if int(''.join(path), 2) < int(''.join(leftmost), 2):
                     leftmost = path
             
             recurse(node.left, path + ['0'])
             recurse(node.right, path + ['1'])
 
         recurse(root, [])
             
         node = root
         while leftmost:
             if leftmost.pop(0) == '0':
                 node = node.left
             else:
                 node = node.right
                 
         return node.val
