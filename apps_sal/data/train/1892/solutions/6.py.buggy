# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         if root is None:
             return []
         if not (root.left or root.right) and root.val == sum:
             return [[root.val]]
         return [[root.val]+ans for ans in self.pathSum(root.left,sum-root.val)+self.pathSum(root.right,sum-root.val)]
