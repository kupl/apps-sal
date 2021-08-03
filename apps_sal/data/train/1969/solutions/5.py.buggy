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
             
             nums += [node.val]
             print(nums)
             
             if not node.left and not node.right:
                 return int(''.join([str(num) for num in nums]))
             
             return sum([
                 traverse(node.left, nums.copy()),
                 traverse(node.right, nums.copy()),
             ])
             
         return traverse(root, [])
