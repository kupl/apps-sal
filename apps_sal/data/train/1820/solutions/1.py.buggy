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
         res = []
         queue = []
         queue.append(root)
         while queue:
             length = len(queue)
             res.append(max([i.val for i in queue]))
             for i in range(length):
                 node = queue.pop(0)
                 if node.left:
                     queue.append(node.left)
                 if node.right:
                     queue.append(node.right)
         return res
