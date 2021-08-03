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
         res = []
 
         def _helper(node, path, tmp_sum):
             if not node:
                 return
             tmp_sum += node.val
             path.append(node.val)
             if tmp_sum == sum and not node.left and not node.right:
                 res.append(path.copy())
             if node.left:
                 _helper(node.left, path, tmp_sum)
             if node.right:
                 _helper(node.right, path, tmp_sum)
             path.pop()
             tmp_sum -= node.val
 
         _helper(root, [], 0)
         return res
