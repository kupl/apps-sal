# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def find(self, root, k):
         if root is None:
             return (None, 0)
         else:
             (v, num), rnum = self.find(root.left, k), 0
             if v is None:
                 v, num = (root.val, 0) if num == k - 1 else (None, num)
                 if v is None:
                     v, rnum = self.find(root.right, k - num - 1)
             return (v, num + rnum + 1)
                 
     
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         return self.find(root, k)[0]
