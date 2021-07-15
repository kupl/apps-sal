# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def countNodes(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         node = root
         depth = 0
         while node:
             depth += 1
             node = node.left
         
         if depth <= 1:
             return depth
         
         lo, hi = 0, 2**(depth-2)
         while lo < hi:
             l = depth-3
             mi = (lo+hi)//2
             node = root
             while l >= 0:
                 d = mi & 2**l
                 node = node.right if d > 0 else node.left
                 l -= 1
             if node.left and node.right:
                 lo = mi+1
             elif not node.left and not node.right:
                 hi = mi
             else:
                 break
         l, node = depth-3, root
         while l >= 0:
             d = mi & 2**l
             node = node.right if d > 0 else node.left
             l -= 1
         return 2**(depth-1)-1 + 2*mi + int(node.left is not None) + int(node.right is not None)
