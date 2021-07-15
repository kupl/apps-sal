# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         def dfs(node, cur_num):
             if node is None: return 0
             my_num = cur_num * 10 + node.val
             if node.left is None and node.right is None: return my_num
             return dfs(node.left, my_num) + dfs(node.right, my_num)
         
         return dfs(root,0)
