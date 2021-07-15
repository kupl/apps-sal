# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     
     def rob2(self, root):
         
         if root is None:
             return (0,0)
         
         with_left, without_left = self.rob2(root.left)
             
         with_right, without_right = self.rob2(root.right)
         
         with_root = without_left + without_right + root.val
         
         without_root = max(with_left, without_left) + max(with_right, without_right)
         
         return (with_root, without_root)
     
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         return max(self.rob2(root))
             
         
