# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def pathSum(self, root, sum):
         """
         :type root: TreeNode
         :type sum: int
         :rtype: List[List[int]]
         """
         if not root:
             return []
         res = []
         q = collections.deque([(root, root.val, [root.val])])
         while q:
             r, v, ls = q.popleft()
             if not r.left and not r.right and v == sum:
                 res.append(ls)
             if r.left:
                 q.append((r.left, v+r.left.val, ls+[r.left.val]))
             if r.right:
                 q.append((r.right, v+r.right.val, ls+[r.right.val]))
         return res
