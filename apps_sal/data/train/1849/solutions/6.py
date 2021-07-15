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
         if root is None:
             return []
         queue = [root]
         result = []
         while len(queue) > 0:
             k = len(queue)
             sublist = []
             for i in range(k):
                 node = queue.pop(0)
                 sublist.append(node.val)
                 if node.left is not None:
                     queue.append(node.left)
                 if node.right is not None:
                     queue.append(node.right)
             result.append(sublist)
         return result
                     
