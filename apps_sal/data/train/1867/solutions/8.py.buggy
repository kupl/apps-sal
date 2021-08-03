# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         stack = []
         curr = root
         count = 0
         while True:
             if curr:
                 stack.append(curr)
                 curr = curr.left
             else:
                 if stack:
                     node = stack.pop()
                     count += 1
                     if count == k: return node.val
                     curr = node.right
                 else:
                     return -1
             
         
