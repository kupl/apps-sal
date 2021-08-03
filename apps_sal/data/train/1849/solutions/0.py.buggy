# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         queue, res = [root], []
         while any(queue):
             tmp = []
             for _ in range(len(queue)):
                 node = queue.pop(0)
                 tmp.append(node.val)
                 if node.left:
                     queue.append(node.left)
                 if node.right:
                     queue.append(node.right)
             res.append(tmp)
         return res
