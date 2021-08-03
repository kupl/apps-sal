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
         ans = []
         buffer = []
         self.helper(ans, root, sum, buffer)
         return ans
     def helper(self, ans, root, sum, buffer):
         """
         recursive method travesal to the bottom of the tree
         and add the path that path's sum equals the given sum into the result
         
         :type ans: List[List[int]]
         :type root: TreeNode
         :type sum: int
         :type buffer: List[int]
         :rtype None
         """
         if not root: return
         sum -= root.val
         buffer.append(root.val)
         if not (root.left or root.right) and sum == 0: ans.append([x for x in buffer])
         self.helper(ans, root.left, sum, buffer)
         self.helper(ans, root.right, sum, buffer)
         buffer.pop()
