# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         def dfs(root):
             if root == None:
                 return [0, 0]
             
             left = dfs(root.left)
             right = dfs(root.right)
             res = [0, 0]
             res[0] = root.val + left[1] + right[1]
             res[1] = max(left[0], left[1]) + max(right[0], right[1])
             return res
         res = dfs(root)
         print(res)
         return max(res[0], res[1])
         
         
