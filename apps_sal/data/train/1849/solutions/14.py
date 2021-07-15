# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 import queue
 
 class Solution(object):
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if not root:
             return []
         
         q = queue.Queue()
         q.put(root)
         ret = []
         while not q.empty():
             nq = queue.Queue()
             level = []
             while not q.empty():
                 node = q.get()
                 level.append(node.val)
                 
                 if node.left:
                     nq.put(node.left)
                 if node.right:
                     nq.put(node.right)
             ret.append(level)
             q = nq
         return ret
         
