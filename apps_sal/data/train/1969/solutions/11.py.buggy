# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from copy import deepcopy
 
 class Solution:
     def __init__(self):
         self.treeSum = 0
         
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.tree(root, [])
         return self.treeSum
     def tree(self, node, path):
         if not node:
             return False
         
         path.append(str(node.val))
         
         print(path, node.val)
         l = self.tree(node.left, copy.deepcopy(path))
         r = self.tree(node.right, copy.deepcopy(path))
         
         if not l and not r:
             self.treeSum += int(''.join(path))
         
         return True
