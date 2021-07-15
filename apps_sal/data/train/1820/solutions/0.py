# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def largestValues(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         if not root:
             return [] 
         q = [root]
         r = []
         while q:
             r.append(max([i.val for i in q]))
             q = [i for node in q for i in [node.left, node.right] if i]
         return r
