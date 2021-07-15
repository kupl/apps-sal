# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import copy
 class Solution:
     def dfs(self, root, sum, cur_path, cur_sum, path):
         if root.left == None and root.right == None:
             if cur_sum + root.val == sum:
                 cur_path.append(root.val)
                 path.append(copy.deepcopy(cur_path))
                 cur_path.pop()
         if root.left != None:
             cur_path.append(root.val)
             self.dfs(root.left, sum, cur_path, cur_sum + root.val, path)
             cur_path.pop()
         if root.right != None:
             cur_path.append(root.val)
             self.dfs(root.right, sum, cur_path, cur_sum + root.val, path)
             cur_path.pop() 
     
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         if root == None:
             return []
         path = []
         self.dfs(root, sum, [], 0, path)
         return path
         
