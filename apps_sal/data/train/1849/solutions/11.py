from queue import Queue
 
 # Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution(object):
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         results = []
         if root is None:
             return results
         q = Queue()
         q.put(root)
         while not q.empty():
             size  = q.qsize()
             sublist = []
             for i in range(size):
                 node = q.get()
                 if node.left is not None:
                     q.put(node.left)
                 if node.right is not None:
                     q.put(node.right)
                 sublist.append(node.val)
             results.append(sublist)
         return results
             
