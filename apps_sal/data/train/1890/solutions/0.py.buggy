# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from collections import deque
 
 class Solution:
     def findBottomLeftValue(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         self.queue = deque([])
         self.queue.append(root)
         return self.bfs()
 
     def bfs(self):
         while len(self.queue):
             node = self.queue.popleft()
             if node.right:
                 self.queue.append(node.right)
             if node.left:
                 self.queue.append(node.left)
         return node.val
         
