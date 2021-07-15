# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import sys
 class Solution:
     def isValidBST(self, root):
         """
         :type root: TreeNode
         :rtype: bool
         """
         if not root or (not root.left and not root.right):
             return True
         return self.isBst(root, [], [])
     def isBst(self, root, min_nums, max_nums):
         # if root:
         #     print("root:", root.val)
         # else:
         #     print("root:", root)
         # print("min_nums", min_nums)
         # print("max_nums", max_nums)
         if not root:
             return True
         min_value = min(min_nums) if min_nums else sys.maxsize
         max_value = max(max_nums) if max_nums else -sys.maxsize-1
         left = self.isBst(root.left, min_nums+[root.val], max_nums)
         right = self.isBst(root.right, min_nums, max_nums+[root.val])
         if root.val < min_value and root.val > max_value and left and right:
             return True
         else:
             return False
             
             
