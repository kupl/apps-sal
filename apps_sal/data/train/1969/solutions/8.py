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
         def traverse(node, nums):
             if node is None:
                 return 0
             
             next_nums = []
             next_nums.extend(nums)
             next_nums.extend([node.val])
             
             if not node.left and not node.right:
                 return int(''.join([str(num) for num in next_nums]))
             
             return sum([
                 traverse(node.left, next_nums),
                 traverse(node.right, next_nums),
             ])
             
         return traverse(root, [])
