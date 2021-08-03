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
         q = [root]
         while any(q):
             res = q[0]
             q = [kid for node in q for kid in (node.left, node.right) if kid]
         return res.val
