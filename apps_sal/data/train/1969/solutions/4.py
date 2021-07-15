# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 def dfs(root,path,sarr):
     
     if root is not None:
         rvalue = path*10+root.val
         if root.left is None and root.right is None:
             sarr+=[rvalue]
         else:
             dfs(root.left,rvalue,sarr)
             dfs(root.right,rvalue,sarr)
 
 class Solution:
     def sumNumbers(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         sarr=[0]
         dfs(root,0,sarr)
         return sum(sarr)
