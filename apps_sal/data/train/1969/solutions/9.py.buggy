# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from copy import deepcopy
 
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.treeSum = 0
         self.tree(root, [])
         return self.treeSum
     def tree(self, node, path):
         if not node:
             return 
         
 
         path.append(str(node.val))
         
         self.tree(node.left, copy.deepcopy(path))
         self.tree(node.right, copy.deepcopy(path))
         
         if not node.left and not node.right:
             self.treeSum += int(''.join(path))
     
 '''
 class Solution:
     def sumNumbers(self, root):
         self.res = 0
         self.dfs(root, 0)
         return self.res
     
     def dfs(self, root, value):
         if root:
             self.dfs(root.left, value*10+root.val)
             self.dfs(root.right, value*10+root.val)
             
             if not root.left and not root.right:
                 self.res += value*10 + root.val
 '''
