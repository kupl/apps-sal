# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from collections import deque
 
 class Solution:
     def zigzagLevelOrder(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[int]]
         """
         if not root:
             return []
         q, d, tmp, ret = deque([]), deque([]),[], []
         q.append(root)
         flag = 1
         while(q or d):
             node = q.popleft()
 
             if node: tmp.append(node.val)
             if node.left: d.append(node.left)
             if node.right: d.append(node.right)
             if not len(q):
                 ret.append(tmp[::flag])
                 q = d
                 d = deque([])
                 tmp = []
                 flag = -flag
             
         return ret
                 
