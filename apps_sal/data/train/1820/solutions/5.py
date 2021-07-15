# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def bfs(self, root):
         queue = [root]
         result = []
         while queue:
             next_q = []
             max_val = -float("inf")
             for node in queue:
                 max_val = max(max_val, node.val)
                 if node.left:
                     next_q.append(node.left)
                 if node.right:
                     next_q.append(node.right)
             result.append(max_val)
             queue = next_q
         return result
         
     def largestValues(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """
         return self.bfs(root) if root else []
         
