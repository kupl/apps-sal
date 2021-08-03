# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 import queue
 
 
 class Solution:
     def levelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         q = queue.Queue()
         q.put(root)
         curNode = root
         levels = []
         while curNode is not None and not q.empty():
             level = []
             newQ = queue.Queue()
             while not q.empty():
                 curNode = q.get()
                 level.append(curNode.val)
                 if curNode.left is not None:
                     newQ.put(curNode.left)
                 if curNode.right is not None:
                     newQ.put(curNode.right)
             levels.append(level)
             q = newQ
         return levels
